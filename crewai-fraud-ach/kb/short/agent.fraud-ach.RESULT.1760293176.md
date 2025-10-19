```json
{
  "id": "5037b957a24a502a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293176,
  "host_pid": "9e6742732c60:1",
  "hash": "ce59c0adcb352c79d4349e27c5fc88a40988a206c46520f2c6e4b6c8bcd6e0e4",
  "cid": "QmV1ce59c0adcb352c79d4349e27c5fc88a40988a206",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293176,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760293176
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "2617420e8de07d2a0170c93efd73a87a3ca02fb284807006275bb675f76a261b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030199431
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 213, 'threshold': 50, 'total_amount': 102689004, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 212, 'first_seen': 1760285763, 'matching_hash': '86eebb6c1a57e398'}}}'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '208726934', 'validation_error': 'Invalid routing number checksum'}}}