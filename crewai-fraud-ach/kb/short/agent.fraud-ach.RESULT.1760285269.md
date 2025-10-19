```json
{
  "id": "8c9be37f1a8171f1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285269,
  "host_pid": "9e6742732c60:1",
  "hash": "594ad0fb2053b0a7e14adfa94a92955da20398671388b72dd5ba63d10ab8a847",
  "cid": "QmV1594ad0fb2053b0a7e14adfa94a92955da2039867",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285269,
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
      "evaluated_at": 1760285269
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "55e3d6c70d451196fbae0db21c4e66bbff8a8267178cf3aa4ac9eaedd8667f3b"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 12220426, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 28, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}