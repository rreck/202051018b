#!/usr/bin/env python3
"""
Synthetic Payment Data Generator
Generates realistic payment transaction data matching the 151-column schema
from AISampleData.xlsx with embedded fraud patterns.
"""

import csv
import hashlib
import random
import string
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from typing import List, Dict, Tuple, Optional
import json


@dataclass
class SyntheticTransaction:
    """Represents a payment transaction matching the 151-column schema"""
    # Transaction fields
    TransactionID: int
    TransactionTypeID: int
    CapturedDate: str
    SettlementDate: str
    SettlementTypeID: int
    CustomerAccountID: int
    CaptureTrackingNumberID: int
    MerchantPayeeCodeID: int
    ProcessorID: int
    DebitCreditTypeID: int
    Amount: float
    CombinedConvenienceFeeToAmount: str
    ConvenienceFee: float
    TransactionReferenceCode: str
    ConfirmationNumber: str
    TransactionStatusTypeID: int
    TransactionSeriesID: int
    TransactionCancelledTypeID: int
    CreditCardAccountID: Optional[int]

    # Card fields
    NameOnCard: str
    AddressLineOne: str
    AddressLineTwo: str
    City: str
    State: str
    ZipCode: str
    ExpirationDate: str
    CardNumberMasked: str
    CardNumberHashed: str
    IsRetired: str
    CreditCardTypeID: int
    IssuingBankName: str

    # Customer fields
    CustomerID: int
    FirstName: str
    MiddleName: str
    LastName: str
    Email: str
    HomePhoneNumber: str

    # Merchant fields
    MerchantID: int
    MerchantName: str
    PayeeCode: str
    PayeeName: str

    # Organization fields
    OrganizationID: int
    OrganizationName: str

    # Metadata for fraud tracking
    is_fraud: bool = False
    fraud_type: str = "LEGITIMATE"
    fraud_score: int = 0
    fraud_flags: List[str] = None

    def __post_init__(self):
        if self.fraud_flags is None:
            self.fraud_flags = []


class SyntheticPaymentGenerator:
    """Generate realistic payment transactions with optional fraud injection"""

    def __init__(self, seed: int = None):
        if seed:
            random.seed(seed)

        self.first_names = [
            "James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda",
            "William", "Barbara", "David", "Elizabeth", "Richard", "Susan", "Joseph",
            "Jessica", "Thomas", "Sarah", "Charles", "Karen", "Christopher", "Nancy"
        ]

        self.last_names = [
            "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
            "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
            "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson"
        ]

        self.merchants = [
            "Amazon", "Walmart", "Target", "Costco", "Home Depot", "Best Buy",
            "CVS Pharmacy", "Walgreens", "Kroger", "Whole Foods", "Starbucks",
            "McDonald's", "Shell Gas", "Exxon", "Netflix", "Apple", "Microsoft"
        ]

        self.banks = [
            "CHASE BANK", "BANK OF AMERICA", "WELLS FARGO", "CITIBANK", "CAPITAL ONE",
            "US BANK", "PNC BANK", "TD BANK", "TRUIST BANK", "FIFTH THIRD BANK",
            "REGIONS BANK", "DISCOVER BANK", "AMERICAN EXPRESS", "SYNCHRONY BANK"
        ]

        self.cities_states = [
            ("New York", "NY"), ("Los Angeles", "CA"), ("Chicago", "IL"), ("Houston", "TX"),
            ("Phoenix", "AZ"), ("Philadelphia", "PA"), ("San Antonio", "TX"), ("San Diego", "CA"),
            ("Dallas", "TX"), ("San Jose", "CA"), ("Austin", "TX"), ("Jacksonville", "FL"),
            ("Fort Worth", "TX"), ("Columbus", "OH"), ("Charlotte", "NC"), ("San Francisco", "CA"),
            ("Indianapolis", "IN"), ("Seattle", "WA"), ("Denver", "CO"), ("Boston", "MA"),
            ("Nashville", "TN"), ("Detroit", "MI"), ("Portland", "OR"), ("Las Vegas", "NV"),
            ("Memphis", "TN"), ("Louisville", "KY"), ("Baltimore", "MD"), ("Milwaukee", "WI"),
            ("Albuquerque", "NM"), ("Tucson", "AZ"), ("Fresno", "CA"), ("Sacramento", "CA"),
            ("Mesa", "AZ"), ("Kansas City", "MO"), ("Atlanta", "GA"), ("Miami", "FL")
        ]

        self.transaction_id_counter = random.randint(4000000, 5000000)
        self.customer_id_counter = random.randint(6000000, 7000000)
        self.card_id_counter = random.randint(6000, 7000)
        self.merchant_id_counter = random.randint(900, 1000)
        self.org_id_counter = random.randint(100000, 110000)

    def _generate_card_number_masked(self) -> str:
        """Generate masked card number (XXXXXXXXXXXX7256 format)"""
        last_four = ''.join([str(random.randint(0, 9)) for _ in range(4)])
        return f"XXXXXXXXXXXX{last_four}"

    def _hash_card_number(self, masked: str) -> str:
        """Generate fake hash for card number"""
        return hashlib.sha256(masked.encode()).hexdigest()[:44]

    def _generate_legitimate_transaction(self, timestamp: datetime) -> SyntheticTransaction:
        """Generate a normal, legitimate transaction"""
        self.transaction_id_counter += 1

        # Customer data
        first_name = random.choice(self.first_names)
        last_name = random.choice(self.last_names)
        customer_id = self.customer_id_counter + random.randint(0, 100000)

        # Card data
        card_id = self.card_id_counter + random.randint(0, 10000)
        card_masked = self._generate_card_number_masked()
        card_hash = self._hash_card_number(card_masked)
        expiration = (timestamp + timedelta(days=random.randint(365, 1095))).strftime("%Y%m%d")

        # Merchant data
        merchant = random.choice(self.merchants)
        merchant_id = self.merchant_id_counter + random.randint(0, 100)

        # Location data
        city, state = random.choice(self.cities_states)
        zipcode = f"{random.randint(10000, 99999)}"

        # Amount: realistic distribution $5-$500, with occasional larger purchases
        if random.random() < 0.05:  # 5% chance of large purchase
            amount = round(random.uniform(500, 2000), 2)
        else:
            amount = round(random.uniform(5, 500), 2)

        # Settlement date: 1-3 days after capture
        settlement_date = timestamp + timedelta(days=random.randint(1, 3))

        return SyntheticTransaction(
            TransactionID=self.transaction_id_counter,
            TransactionTypeID=1,
            CapturedDate=timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            SettlementDate=settlement_date.strftime("%Y-%m-%d %H:%M:%S"),
            SettlementTypeID=2,
            CustomerAccountID=customer_id + random.randint(0, 10),
            CaptureTrackingNumberID=random.randint(240000, 250000),
            MerchantPayeeCodeID=merchant_id,
            ProcessorID=234,
            DebitCreditTypeID=1,
            Amount=amount,
            CombinedConvenienceFeeToAmount="False",
            ConvenienceFee=0.0,
            TransactionReferenceCode=f"TX{timestamp.strftime('%Y%m%d%H%M%S')}{random.randint(100,999)}",
            ConfirmationNumber=f"CNF{timestamp.strftime('%Y%m%d%H%M%S')}{random.randint(100,999)}",
            TransactionStatusTypeID=5,  # Approved
            TransactionSeriesID=random.randint(6000, 7000),
            TransactionCancelledTypeID=0,
            CreditCardAccountID=card_id,
            NameOnCard=f"{first_name} {last_name}",
            AddressLineOne=f"{random.randint(100, 9999)} {random.choice(['Main', 'Oak', 'Maple', 'Pine', 'Elm'])} St",
            AddressLineTwo="",
            City=city,
            State=state,
            ZipCode=zipcode,
            ExpirationDate=expiration,
            CardNumberMasked=card_masked,
            CardNumberHashed=card_hash,
            IsRetired="False",
            CreditCardTypeID=random.choice([1, 2]),  # 1=Visa, 2=MasterCard
            IssuingBankName=random.choice(self.banks),
            CustomerID=customer_id,
            FirstName=first_name,
            MiddleName="",
            LastName=last_name,
            Email=f"{first_name.lower()}.{last_name.lower()}@example.com",
            HomePhoneNumber=f"{random.randint(200,999)}{random.randint(2000000,9999999)}",
            MerchantID=merchant_id,
            MerchantName=merchant,
            PayeeCode=merchant[:2].upper(),
            PayeeName=merchant,
            OrganizationID=self.org_id_counter,
            OrganizationName="Payment Processor Inc",
            is_fraud=False,
            fraud_type="LEGITIMATE",
            fraud_score=0
        )

    def _generate_card_testing_fraud(self, timestamp: datetime, base_card_id: int, sequence: int) -> SyntheticTransaction:
        """Generate card testing fraud transaction"""
        self.transaction_id_counter += 1

        # Card testing: small amounts, rapid succession, same card
        txn = self._generate_legitimate_transaction(timestamp)

        # Override with card testing characteristics
        txn.Amount = round(random.uniform(0.50, 5.00), 2)  # Very small amounts
        txn.CreditCardAccountID = base_card_id  # Same card
        txn.TransactionStatusTypeID = 6 if sequence < 3 else 5  # First few declined, then approved
        txn.is_fraud = True
        txn.fraud_type = "CARD_TESTING"
        txn.fraud_score = 85

        # Build fraud flags
        flags = []
        if txn.Amount < 5.0:
            flags.append("card_testing_small_amount")
        if sequence >= 3:
            flags.append("card_testing_rapid_succession")
        if txn.TransactionStatusTypeID == 6:
            flags.append("card_testing_mixed_decline_approve")

        txn.fraud_flags = flags

        return txn

    def generate_dataset(self,
                        transaction_count: int = 1000,
                        fraud_type: str = "card_testing",
                        fraud_intensity: float = 0.10) -> List[SyntheticTransaction]:
        """
        Generate synthetic dataset with fraud patterns

        Args:
            transaction_count: Total number of transactions to generate
            fraud_type: Type of fraud to inject (card_testing, etc.)
            fraud_intensity: Ratio of fraudulent transactions (0.0-1.0)

        Returns:
            List of synthetic transactions
        """
        transactions = []
        fraud_count = int(transaction_count * fraud_intensity)

        # Generate timeline: transactions over 24 hours
        start_time = datetime.now() - timedelta(days=1)

        if fraud_type == "card_testing":
            # Generate card testing attack: clusters of rapid small transactions
            attack_count = fraud_count // 5  # Each attack is ~5 transactions
            attack_indices = random.sample(range(transaction_count), attack_count)

            current_time = start_time
            transaction_index = 0

            for i in range(transaction_count):
                # Time increment: most transactions spread out, attacks compressed
                if i in attack_indices:
                    # Start of card testing attack
                    base_card_id = self.card_id_counter + random.randint(0, 10000)
                    for seq in range(5):  # 5 rapid transactions
                        if transaction_index >= transaction_count:
                            break
                        # Very short time gaps (seconds to minutes)
                        current_time += timedelta(seconds=random.randint(10, 120))
                        txn = self._generate_card_testing_fraud(current_time, base_card_id, seq)
                        transactions.append(txn)
                        transaction_index += 1
                else:
                    # Normal transaction
                    current_time += timedelta(minutes=random.randint(1, 60))
                    txn = self._generate_legitimate_transaction(current_time)
                    transactions.append(txn)
                    transaction_index += 1

                if transaction_index >= transaction_count:
                    break
        else:
            # Default: randomly distributed fraud
            fraud_indices = set(random.sample(range(transaction_count), fraud_count))
            current_time = start_time

            for i in range(transaction_count):
                current_time += timedelta(minutes=random.randint(1, 60))
                if i in fraud_indices:
                    # Generic fraud transaction
                    txn = self._generate_legitimate_transaction(current_time)
                    txn.is_fraud = True
                    txn.fraud_type = "UNKNOWN"
                    txn.fraud_score = 60
                else:
                    txn = self._generate_legitimate_transaction(current_time)

                transactions.append(txn)

        return transactions[:transaction_count]

    def save_to_csv(self, transactions: List[SyntheticTransaction], output_path: str):
        """Save transactions to CSV file"""
        if not transactions:
            return

        # Define simplified columns for CSV output
        fieldnames = [
            'TransactionID', 'CapturedDate', 'SettlementDate', 'Amount',
            'TransactionStatusTypeID', 'CreditCardAccountID', 'CardNumberMasked',
            'NameOnCard', 'City', 'State', 'ZipCode', 'MerchantName',
            'IssuingBankName', 'FirstName', 'LastName', 'Email',
            'is_fraud', 'fraud_type', 'fraud_score', 'fraud_flags'
        ]

        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for txn in transactions:
                row = {
                    'TransactionID': txn.TransactionID,
                    'CapturedDate': txn.CapturedDate,
                    'SettlementDate': txn.SettlementDate,
                    'Amount': txn.Amount,
                    'TransactionStatusTypeID': txn.TransactionStatusTypeID,
                    'CreditCardAccountID': txn.CreditCardAccountID,
                    'CardNumberMasked': txn.CardNumberMasked,
                    'NameOnCard': txn.NameOnCard,
                    'City': txn.City,
                    'State': txn.State,
                    'ZipCode': txn.ZipCode,
                    'MerchantName': txn.MerchantName,
                    'IssuingBankName': txn.IssuingBankName,
                    'FirstName': txn.FirstName,
                    'LastName': txn.LastName,
                    'Email': txn.Email,
                    'is_fraud': txn.is_fraud,
                    'fraud_type': txn.fraud_type,
                    'fraud_score': txn.fraud_score,
                    'fraud_flags': '|'.join(txn.fraud_flags) if txn.fraud_flags else ''
                }
                writer.writerow(row)

    def save_ground_truth(self, transactions: List[SyntheticTransaction], output_path: str):
        """Save ground truth labels for evaluation"""
        ground_truth = []
        for txn in transactions:
            ground_truth.append({
                'transaction_id': txn.TransactionID,
                'is_fraud': txn.is_fraud,
                'fraud_type': txn.fraud_type,
                'fraud_score': txn.fraud_score,
                'fraud_flags': txn.fraud_flags
            })

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump({
                'transaction_count': len(transactions),
                'fraud_count': sum(1 for t in transactions if t.is_fraud),
                'ground_truth': ground_truth
            }, f, indent=2)
