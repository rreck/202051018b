```json
{
  "id": "6579f0b3cfa36d80",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294175,
  "host_pid": "9e6742732c60:1",
  "hash": "4a61c4128601c51f55cefde8706ffd9b4e652a89639d58ca19462372c9bca911",
  "cid": "QmV14a61c4128601c51f55cefde8706ffd9b4e652a89",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294175,
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
      "evaluated_at": 1760294175
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
  "sig": "cd23ef0e747564932758837380e3382ca62dac613435c5881c358ef6381c70bc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245124241
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 75823559, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760285764, 'matching_hash': '1e6f1dd53bdf6417'}}}