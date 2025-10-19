```json
{
  "id": "44d7ccb4fb548f5f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291448,
  "host_pid": "9e6742732c60:1",
  "hash": "f04c0ef5aeef7fd7ee4bde587552d7395d568f6bc72d56320684ca7276068811",
  "cid": "QmV1f04c0ef5aeef7fd7ee4bde587552d7395d568f6b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291448,
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
      "evaluated_at": 1760291448
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
  "sig": "3e015dfff54e66d325caf0ae49cd94a7bd5e61148c70415bdbddd098096739b0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464946217
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 251, 'threshold': 50, 'total_amount': 85426093, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 250, 'first_seen': 1760284979, 'matching_hash': '76eefa6b67e55304'}}}