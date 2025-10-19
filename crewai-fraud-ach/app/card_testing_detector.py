#!/usr/bin/env python3
"""
Card Testing Fraud Detection Engine
Implements scoring system (0-100) with pattern flags for card testing detection
"""

import csv
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict, Tuple, Optional


@dataclass
class TransactionRecord:
    """Transaction record for analysis"""
    transaction_id: int
    captured_date: datetime
    amount: float
    status_type_id: int
    card_id: int
    card_masked: str
    merchant_name: str
    customer_name: str

    @classmethod
    def from_csv_row(cls, row: Dict):
        """Create from CSV row"""
        return cls(
            transaction_id=int(row['TransactionID']),
            captured_date=datetime.fromisoformat(row['CapturedDate']),
            amount=float(row['Amount']),
            status_type_id=int(row['TransactionStatusTypeID']),
            card_id=int(row['CreditCardAccountID']),
            card_masked=row['CardNumberMasked'],
            merchant_name=row['MerchantName'],
            customer_name=row['NameOnCard']
        )


@dataclass
class DetectionResult:
    """Result of fraud detection analysis"""
    transaction_id: int
    fraud_score: int  # 0-100
    fraud_detected: bool  # True if score >= threshold
    pattern_flags: List[str]
    risk_level: str  # LOW, MEDIUM, HIGH, CRITICAL
    details: Dict

    def to_dict(self) -> Dict:
        return {
            'transaction_id': self.transaction_id,
            'fraud_score': self.fraud_score,
            'fraud_detected': self.fraud_detected,
            'pattern_flags': self.pattern_flags,
            'risk_level': self.risk_level,
            'details': self.details
        }


class CardTestingDetector:
    """
    Card Testing Fraud Detector

    Implements:
    - Fraud scoring (0-100)
    - Pattern flag detection
    - Configurable threshold (default 75)
    """

    def __init__(self, threshold: int = 75):
        self.threshold = threshold
        self.card_history = defaultdict(list)  # card_id -> [transactions]

    def analyze_transaction(self, txn: TransactionRecord) -> DetectionResult:
        """
        Analyze single transaction for card testing patterns

        Returns DetectionResult with score and flags
        """
        score = 0
        flags = []
        details = {}

        # Track transaction by card
        self.card_history[txn.card_id].append(txn)
        card_txns = self.card_history[txn.card_id]

        # Pattern 1: Small amount (< $5)
        if txn.amount < 5.0:
            score += 25
            flags.append("card_testing_small_amount")
            details['small_amount'] = f"${txn.amount:.2f} < $5.00"

        # Pattern 2: Rapid succession (5+ txns in <10 minutes)
        recent_txns = [
            t for t in card_txns
            if (txn.captured_date - t.captured_date).total_seconds() < 600  # 10 min
        ]
        if len(recent_txns) >= 5:
            score += 35
            flags.append("card_testing_rapid_succession")
            details['rapid_succession'] = f"{len(recent_txns)} txns in <10 min"

        # Pattern 3: Mixed decline/approve pattern
        if len(card_txns) >= 3:
            last_3_statuses = [t.status_type_id for t in card_txns[-3:]]
            # Status 6 = declined, 5 = approved
            if 6 in last_3_statuses and 5 in last_3_statuses:
                score += 30
                flags.append("card_testing_mixed_decline_approve")
                details['mixed_status'] = f"Statuses: {last_3_statuses}"

        # Pattern 4: Multiple merchants quickly (velocity check)
        recent_hour = [
            t for t in card_txns
            if (txn.captured_date - t.captured_date).total_seconds() < 3600
        ]
        unique_merchants = len(set(t.merchant_name for t in recent_hour))
        if unique_merchants >= 3:
            score += 20
            flags.append("card_testing_merchant_diversity")
            details['merchant_diversity'] = f"{unique_merchants} merchants in 1hr"

        # Pattern 5: High transaction velocity (>10 txns/hour)
        if len(recent_hour) > 10:
            score += 25
            flags.append("card_testing_velocity")
            details['velocity'] = f"{len(recent_hour)} txns/hour"

        # Cap score at 100
        score = min(score, 100)

        # Determine risk level
        if score >= 90:
            risk_level = "CRITICAL"
        elif score >= 75:
            risk_level = "HIGH"
        elif score >= 50:
            risk_level = "MEDIUM"
        else:
            risk_level = "LOW"

        fraud_detected = score >= self.threshold

        return DetectionResult(
            transaction_id=txn.transaction_id,
            fraud_score=score,
            fraud_detected=fraud_detected,
            pattern_flags=flags,
            risk_level=risk_level,
            details=details
        )

    def analyze_batch(self, csv_path: str) -> List[DetectionResult]:
        """Analyze entire CSV file of transactions"""
        results = []

        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                txn = TransactionRecord.from_csv_row(row)
                result = self.analyze_transaction(txn)
                results.append(result)

        return results

    def calculate_confusion_matrix(self,
                                   results: List[DetectionResult],
                                   ground_truth_path: str) -> Dict:
        """
        Calculate confusion matrix comparing detections to ground truth

        Returns:
            {
                'true_positives': int,
                'false_positives': int,
                'true_negatives': int,
                'false_negatives': int,
                'accuracy': float,
                'precision': float,
                'recall': float
            }
        """
        import json

        # Load ground truth
        with open(ground_truth_path, 'r') as f:
            ground_truth_data = json.load(f)

        # Create lookup
        ground_truth = {}
        for item in ground_truth_data['ground_truth']:
            ground_truth[item['transaction_id']] = item['is_fraud']

        # Calculate confusion matrix
        tp = 0  # True Positive: detected fraud, was fraud
        fp = 0  # False Positive: detected fraud, was clean
        tn = 0  # True Negative: no detection, was clean
        fn = 0  # False Negative: no detection, was fraud

        for result in results:
            actual_fraud = ground_truth.get(result.transaction_id, False)
            predicted_fraud = result.fraud_detected

            if predicted_fraud and actual_fraud:
                tp += 1
            elif predicted_fraud and not actual_fraud:
                fp += 1
            elif not predicted_fraud and not actual_fraud:
                tn += 1
            elif not predicted_fraud and actual_fraud:
                fn += 1

        # Calculate metrics
        total = tp + fp + tn + fn
        accuracy = (tp + tn) / total if total > 0 else 0.0
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0

        return {
            'true_positives': tp,
            'false_positives': fp,
            'true_negatives': tn,
            'false_negatives': fn,
            'accuracy': round(accuracy, 4),
            'precision': round(precision, 4),
            'recall': round(recall, 4),
            'f1_score': round(f1_score, 4),
            'total_transactions': total
        }

    def get_score_distribution(self, results: List[DetectionResult]) -> Dict:
        """Get distribution of fraud scores"""
        distribution = {
            '0-25': 0,
            '26-50': 0,
            '51-75': 0,
            '76-100': 0
        }

        for result in results:
            score = result.fraud_score
            if score <= 25:
                distribution['0-25'] += 1
            elif score <= 50:
                distribution['26-50'] += 1
            elif score <= 75:
                distribution['51-75'] += 1
            else:
                distribution['76-100'] += 1

        return distribution

    def get_pattern_flag_counts(self, results: List[DetectionResult]) -> Dict:
        """Count occurrences of each pattern flag"""
        flag_counts = defaultdict(int)

        for result in results:
            for flag in result.pattern_flags:
                flag_counts[flag] += 1

        return dict(flag_counts)
