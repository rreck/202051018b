```json
{
  "id": "b08cf13aac3afb95",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289035,
  "host_pid": "9e6742732c60:1",
  "hash": "9ee9f14c52ea25f30ef0ec2bf4e6158f02e4d1fc8b2353e4e640eaf2ab1fa1c3",
  "cid": "QmV19ee9f14c52ea25f30ef0ec2bf4e6158f02e4d1fc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289035,
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
      "evaluated_at": 1760289035
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
  "sig": "3f4718a87390e76cc9f02c0546841bec8d20199de6d56cb848afdf0040f0f268"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023496704
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 111, 'threshold': 50, 'total_amount': 37634883, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 110, 'first_seen': 1760285765, 'matching_hash': 'f379baac52e28232'}}}