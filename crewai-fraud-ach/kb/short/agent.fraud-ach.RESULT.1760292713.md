```json
{
  "id": "32f442f303b0fb45",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292713,
  "host_pid": "9e6742732c60:1",
  "hash": "b90d4e773657679b554a7dfaa304e45bc06cf5be5e58a61474f86e046c143da9",
  "cid": "QmV1b90d4e773657679b554a7dfaa304e45bc06cf5be",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292713,
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
      "evaluated_at": 1760292713
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
  "sig": "e88aa409965504eaf8d724021c9cc603da742eedcba2c910f8d49c8fe7661491"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463882943
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 203, 'threshold': 50, 'total_amount': 25173624, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 202, 'first_seen': 1760285765, 'matching_hash': '0eb18222520b1d39'}}}