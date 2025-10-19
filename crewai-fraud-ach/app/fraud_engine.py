#!/usr/bin/env python3
# -----------------------------------------------------------------------------
# Copyright (c) RRECKTEK LLC
# Project: CrewAI Fraud Detection Agent - Fraud Detection Engine
# Version: 1.0.0
#
# Purpose:
#   Fraud detection engine for ACH transactions. Implements multiple
#   detection strategies:
#   - Velocity checks: Transaction rate limits per account/routing
#   - Duplicate detection: Hash-based duplicate transaction identification
#   - Amount anomalies: Statistical outlier detection (Z-score, IQR)
#   - Routing validation: ABA routing number checksum and OFAC simulation
#   - Pattern recognition: Round amounts, sequential IDs, off-hours batches
#   - Risk scoring: 0-100 scale with configurable thresholds
# -----------------------------------------------------------------------------

import hashlib
import statistics
from collections import defaultdict
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import time
import re

from ach_schema import validate_routing_number, TransactionCode


class FraudType:
    """Fraud type constants"""
    VELOCITY_ATTACK = 'velocity_attack'
    DUPLICATE_TRANSACTION = 'duplicate_transaction'
    AMOUNT_ANOMALY = 'amount_anomaly'
    INVALID_ROUTING = 'invalid_routing'
    ROUND_AMOUNT_PATTERN = 'round_amount_pattern'
    SEQUENTIAL_ID_PATTERN = 'sequential_id_pattern'
    OFF_HOURS_BATCH = 'off_hours_batch'
    SUSPICIOUS_PATTERN = 'suspicious_pattern'
    LEGITIMATE = 'legitimate'

    ALL_TYPES = [
        VELOCITY_ATTACK,
        DUPLICATE_TRANSACTION,
        AMOUNT_ANOMALY,
        INVALID_ROUTING,
        ROUND_AMOUNT_PATTERN,
        SEQUENTIAL_ID_PATTERN,
        OFF_HOURS_BATCH,
        SUSPICIOUS_PATTERN,
        LEGITIMATE
    ]


class FraudDetectionConfig:
    """Configuration for fraud detection thresholds"""

    def __init__(self):
        # Velocity thresholds
        self.velocity_window_seconds = 7 * 24 * 3600  # 7 days
        self.velocity_max_transactions_per_account = 50
        self.velocity_max_amount_per_account = 100000_00  # $100,000 in cents

        # Duplicate detection
        self.duplicate_window_seconds = 24 * 3600  # 24 hours
        self.duplicate_tolerance_cents = 0  # Exact match

        # Amount anomaly thresholds
        self.amount_zscore_threshold = 3.0  # Standard deviations
        self.amount_iqr_multiplier = 1.5
        self.amount_minimum_samples = 10  # Need this many samples for statistics

        # Pattern recognition
        self.round_amount_threshold = 5000_00  # $50 and above
        self.off_hours_start = 0  # Midnight
        self.off_hours_end = 6  # 6 AM

        # Risk scoring thresholds
        self.risk_low_threshold = 30
        self.risk_medium_threshold = 60
        self.risk_high_threshold = 80

        # OFAC simulation (in real system, this would be actual OFAC screening)
        self.ofac_simulation_keywords = [
            'SANCTIONED',
            'BLOCKED',
            'TERRORIST',
            'EMBARGO',
            'PROHIBITED'
        ]


class TransactionRecord:
    """Transaction record for fraud analysis"""

    def __init__(self,
                 transaction_id: str,
                 timestamp: int,  # EPOCH
                 routing_number: str,
                 account_number: str,
                 amount: int,  # In cents
                 transaction_code: str,
                 individual_name: str,
                 individual_id: str,
                 trace_number: str,
                 batch_timestamp: Optional[int] = None):
        self.transaction_id = transaction_id
        self.timestamp = timestamp
        self.routing_number = routing_number
        self.account_number = account_number
        self.amount = amount
        self.transaction_code = transaction_code
        self.individual_name = individual_name
        self.individual_id = individual_id
        self.trace_number = trace_number
        self.batch_timestamp = batch_timestamp or timestamp

        # Computed fields
        self.hash = self._compute_hash()

    def _compute_hash(self) -> str:
        """Compute unique hash for duplicate detection"""
        components = [
            self.routing_number,
            self.account_number,
            str(self.amount),
            self.transaction_code,
            self.individual_name,
        ]
        hash_input = '|'.join(components)
        return hashlib.sha256(hash_input.encode('utf-8')).hexdigest()

    def is_debit(self) -> bool:
        """Check if transaction is a debit"""
        return self.transaction_code in TransactionCode.DEBIT_CODES


class FraudDetectionResult:
    """Result of fraud detection analysis"""

    def __init__(self,
                 transaction_id: str,
                 fraud_detected: bool,
                 fraud_types: List[str],
                 risk_score: int,  # 0-100
                 risk_level: str,  # 'low', 'medium', 'high', 'critical'
                 details: Dict,
                 timestamp: int):
        self.transaction_id = transaction_id
        self.fraud_detected = fraud_detected
        self.fraud_types = fraud_types
        self.risk_score = risk_score
        self.risk_level = risk_level
        self.details = details
        self.timestamp = timestamp

    def to_dict(self) -> Dict:
        """Convert to dictionary for serialization"""
        return {
            'transaction_id': self.transaction_id,
            'fraud_detected': self.fraud_detected,
            'fraud_types': self.fraud_types,
            'risk_score': self.risk_score,
            'risk_level': self.risk_level,
            'details': self.details,
            'timestamp': self.timestamp
        }


class FraudDetectionEngine:
    """Main fraud detection engine"""

    def __init__(self, config: Optional[FraudDetectionConfig] = None):
        self.config = config or FraudDetectionConfig()

        # Transaction history for velocity and pattern detection
        self.transaction_history: List[TransactionRecord] = []
        self.transaction_hashes: Dict[str, List[TransactionRecord]] = defaultdict(list)

        # Account tracking
        self.account_transactions: Dict[str, List[TransactionRecord]] = defaultdict(list)
        self.routing_transactions: Dict[str, List[TransactionRecord]] = defaultdict(list)

        # Statistics cache
        self.amount_statistics: Optional[Dict] = None
        self.statistics_valid_until: int = 0

    def analyze_transaction(self, transaction: TransactionRecord) -> FraudDetectionResult:
        """Analyze a single transaction for fraud indicators"""
        fraud_types = []
        risk_components = []
        details = {}

        # 1. Velocity check
        velocity_result = self._check_velocity(transaction)
        if velocity_result['fraud_detected']:
            fraud_types.append(FraudType.VELOCITY_ATTACK)
            risk_components.append(velocity_result['risk_score'])
            details['velocity'] = velocity_result

        # 2. Duplicate detection
        duplicate_result = self._check_duplicate(transaction)
        if duplicate_result['fraud_detected']:
            fraud_types.append(FraudType.DUPLICATE_TRANSACTION)
            risk_components.append(duplicate_result['risk_score'])
            details['duplicate'] = duplicate_result

        # 3. Routing validation
        routing_result = self._check_routing(transaction)
        if routing_result['fraud_detected']:
            fraud_types.append(FraudType.INVALID_ROUTING)
            risk_components.append(routing_result['risk_score'])
            details['routing'] = routing_result

        # 4. Amount anomaly detection
        anomaly_result = self._check_amount_anomaly(transaction)
        if anomaly_result['fraud_detected']:
            fraud_types.append(FraudType.AMOUNT_ANOMALY)
            risk_components.append(anomaly_result['risk_score'])
            details['amount_anomaly'] = anomaly_result

        # 5. Round amount pattern
        round_amount_result = self._check_round_amount(transaction)
        if round_amount_result['fraud_detected']:
            fraud_types.append(FraudType.ROUND_AMOUNT_PATTERN)
            risk_components.append(round_amount_result['risk_score'])
            details['round_amount'] = round_amount_result

        # 6. Off-hours batch check
        off_hours_result = self._check_off_hours(transaction)
        if off_hours_result['fraud_detected']:
            fraud_types.append(FraudType.OFF_HOURS_BATCH)
            risk_components.append(off_hours_result['risk_score'])
            details['off_hours'] = off_hours_result

        # 7. OFAC simulation
        ofac_result = self._check_ofac_simulation(transaction)
        if ofac_result['fraud_detected']:
            fraud_types.append(FraudType.SUSPICIOUS_PATTERN)
            risk_components.append(ofac_result['risk_score'])
            details['ofac'] = ofac_result

        # Calculate overall risk score
        if risk_components:
            risk_score = min(100, int(sum(risk_components) / len(risk_components)))
        else:
            risk_score = 0

        # Determine risk level
        if risk_score >= self.config.risk_high_threshold:
            risk_level = 'critical'
        elif risk_score >= self.config.risk_medium_threshold:
            risk_level = 'high'
        elif risk_score >= self.config.risk_low_threshold:
            risk_level = 'medium'
        else:
            risk_level = 'low'

        # Record transaction in history
        self._record_transaction(transaction)

        return FraudDetectionResult(
            transaction_id=transaction.transaction_id,
            fraud_detected=len(fraud_types) > 0,
            fraud_types=fraud_types if fraud_types else [FraudType.LEGITIMATE],
            risk_score=risk_score,
            risk_level=risk_level,
            details=details,
            timestamp=int(time.time())
        )

    def _check_velocity(self, transaction: TransactionRecord) -> Dict:
        """Check for velocity attack patterns"""
        result = {'fraud_detected': False, 'risk_score': 0, 'details': {}}

        # Get recent transactions for this account
        account_key = f"{transaction.routing_number}:{transaction.account_number}"
        window_start = transaction.timestamp - self.config.velocity_window_seconds

        recent_transactions = [
            t for t in self.account_transactions[account_key]
            if t.timestamp >= window_start
        ]

        # Check transaction count
        transaction_count = len(recent_transactions) + 1  # +1 for current
        if transaction_count > self.config.velocity_max_transactions_per_account:
            result['fraud_detected'] = True
            result['risk_score'] = min(100, 50 + (transaction_count - self.config.velocity_max_transactions_per_account) * 2)
            result['details']['transaction_count'] = transaction_count
            result['details']['threshold'] = self.config.velocity_max_transactions_per_account

        # Check total amount
        total_amount = sum(t.amount for t in recent_transactions) + transaction.amount
        if total_amount > self.config.velocity_max_amount_per_account:
            result['fraud_detected'] = True
            result['risk_score'] = max(result['risk_score'], 70)
            result['details']['total_amount'] = total_amount
            result['details']['amount_threshold'] = self.config.velocity_max_amount_per_account

        return result

    def _check_duplicate(self, transaction: TransactionRecord) -> Dict:
        """Check for duplicate transactions"""
        result = {'fraud_detected': False, 'risk_score': 0, 'details': {}}

        window_start = transaction.timestamp - self.config.duplicate_window_seconds

        # Check hash history
        similar_transactions = [
            t for t in self.transaction_hashes[transaction.hash]
            if t.timestamp >= window_start
        ]

        if similar_transactions:
            result['fraud_detected'] = True
            result['risk_score'] = 85
            result['details']['duplicate_count'] = len(similar_transactions)
            result['details']['first_seen'] = similar_transactions[0].timestamp
            result['details']['matching_hash'] = transaction.hash[:16]

        return result

    def _check_routing(self, transaction: TransactionRecord) -> Dict:
        """Validate routing number"""
        result = {'fraud_detected': False, 'risk_score': 0, 'details': {}}

        if not validate_routing_number(transaction.routing_number):
            result['fraud_detected'] = True
            result['risk_score'] = 95
            result['details']['routing_number'] = transaction.routing_number
            result['details']['validation_error'] = 'Invalid routing number checksum'

        return result

    def _check_amount_anomaly(self, transaction: TransactionRecord) -> Dict:
        """Detect amount anomalies using statistical methods"""
        result = {'fraud_detected': False, 'risk_score': 0, 'details': {}}

        # Need enough historical data
        if len(self.transaction_history) < self.config.amount_minimum_samples:
            return result

        # Refresh statistics if needed
        current_time = int(time.time())
        if current_time > self.statistics_valid_until:
            self._compute_amount_statistics()

        if not self.amount_statistics:
            return result

        amount = transaction.amount
        mean = self.amount_statistics['mean']
        stdev = self.amount_statistics['stdev']
        q1 = self.amount_statistics['q1']
        q3 = self.amount_statistics['q3']
        iqr = q3 - q1

        # Z-score method
        if stdev > 0:
            zscore = abs((amount - mean) / stdev)
            if zscore > self.config.amount_zscore_threshold:
                result['fraud_detected'] = True
                result['risk_score'] = min(100, int(40 + zscore * 10))
                result['details']['zscore'] = round(zscore, 2)
                result['details']['mean'] = mean
                result['details']['stdev'] = stdev

        # IQR method
        lower_bound = q1 - self.config.amount_iqr_multiplier * iqr
        upper_bound = q3 + self.config.amount_iqr_multiplier * iqr
        if amount < lower_bound or amount > upper_bound:
            result['fraud_detected'] = True
            result['risk_score'] = max(result['risk_score'], 60)
            result['details']['iqr_bounds'] = {'lower': lower_bound, 'upper': upper_bound}
            result['details']['amount'] = amount

        return result

    def _check_round_amount(self, transaction: TransactionRecord) -> Dict:
        """Detect suspiciously round amounts"""
        result = {'fraud_detected': False, 'risk_score': 0, 'details': {}}

        amount = transaction.amount

        # Check if amount is exactly divisible by large round numbers
        if amount >= self.config.round_amount_threshold:
            if amount % 100000 == 0:  # Exactly $1000
                result['fraud_detected'] = True
                result['risk_score'] = 40
                result['details']['pattern'] = 'exact_thousands'
            elif amount % 50000 == 0:  # Exactly $500
                result['fraud_detected'] = True
                result['risk_score'] = 30
                result['details']['pattern'] = 'exact_five_hundreds'
            elif amount % 10000 == 0:  # Exactly $100
                result['fraud_detected'] = True
                result['risk_score'] = 20
                result['details']['pattern'] = 'exact_hundreds'

            if result['fraud_detected']:
                result['details']['amount'] = amount

        return result

    def _check_off_hours(self, transaction: TransactionRecord) -> Dict:
        """Check if batch was submitted during unusual hours"""
        result = {'fraud_detected': False, 'risk_score': 0, 'details': {}}

        batch_dt = datetime.fromtimestamp(transaction.batch_timestamp)
        hour = batch_dt.hour

        if self.config.off_hours_start <= hour < self.config.off_hours_end:
            result['fraud_detected'] = True
            result['risk_score'] = 35
            result['details']['batch_hour'] = hour
            result['details']['batch_timestamp'] = transaction.batch_timestamp

        return result

    def _check_ofac_simulation(self, transaction: TransactionRecord) -> Dict:
        """Simulate OFAC screening (in production, use real OFAC data)"""
        result = {'fraud_detected': False, 'risk_score': 0, 'details': {}}

        name_upper = transaction.individual_name.upper()

        for keyword in self.config.ofac_simulation_keywords:
            if keyword in name_upper:
                result['fraud_detected'] = True
                result['risk_score'] = 100
                result['details']['ofac_match'] = keyword
                result['details']['individual_name'] = transaction.individual_name
                break

        return result

    def _compute_amount_statistics(self):
        """Compute statistical measures for amount anomaly detection"""
        if len(self.transaction_history) < self.config.amount_minimum_samples:
            return

        amounts = [t.amount for t in self.transaction_history]

        self.amount_statistics = {
            'mean': statistics.mean(amounts),
            'median': statistics.median(amounts),
            'stdev': statistics.stdev(amounts) if len(amounts) > 1 else 0,
            'q1': statistics.quantiles(amounts, n=4)[0],
            'q3': statistics.quantiles(amounts, n=4)[2],
            'min': min(amounts),
            'max': max(amounts),
            'count': len(amounts)
        }

        # Cache valid for 1 hour
        self.statistics_valid_until = int(time.time()) + 3600

    def _record_transaction(self, transaction: TransactionRecord):
        """Record transaction in history for future analysis"""
        self.transaction_history.append(transaction)
        self.transaction_hashes[transaction.hash].append(transaction)

        account_key = f"{transaction.routing_number}:{transaction.account_number}"
        self.account_transactions[account_key].append(transaction)
        self.routing_transactions[transaction.routing_number].append(transaction)

        # Prune old transactions (older than velocity window)
        cutoff_time = transaction.timestamp - self.config.velocity_window_seconds
        self.transaction_history = [
            t for t in self.transaction_history
            if t.timestamp >= cutoff_time
        ]

    def get_statistics(self) -> Dict:
        """Get detection statistics"""
        fraud_counts = defaultdict(int)
        total_transactions = len(self.transaction_history)

        return {
            'total_transactions_analyzed': total_transactions,
            'fraud_type_counts': dict(fraud_counts),
            'unique_accounts': len(self.account_transactions),
            'unique_routing_numbers': len(self.routing_transactions),
            'amount_statistics': self.amount_statistics or {},
            'detection_config': {
                'velocity_max_transactions': self.config.velocity_max_transactions_per_account,
                'velocity_window_days': self.config.velocity_window_seconds / (24 * 3600),
                'duplicate_window_hours': self.config.duplicate_window_seconds / 3600,
                'zscore_threshold': self.config.amount_zscore_threshold,
            }
        }

    def reset(self):
        """Reset detection engine state"""
        self.transaction_history.clear()
        self.transaction_hashes.clear()
        self.account_transactions.clear()
        self.routing_transactions.clear()
        self.amount_statistics = None
        self.statistics_valid_until = 0
