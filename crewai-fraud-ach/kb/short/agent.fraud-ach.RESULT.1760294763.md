```json
{
  "id": "e8db2d3112fd28c0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294763,
  "host_pid": "9e6742732c60:1",
  "hash": "b9b70d03b8a9a47e2825a77111dae00061e96e52ffe9b7bbd89316f08b15865d",
  "cid": "QmV1b9b70d03b8a9a47e2825a77111dae00061e96e52",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294763,
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
      "evaluated_at": 1760294763
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
  "sig": "95be6dac21b13cb4fd209ab0395138783b567e684a6bee0551413bcbfccb02f5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469153369
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 22148368, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285764, 'matching_hash': 'a6e88c6efc20349f'}}}}