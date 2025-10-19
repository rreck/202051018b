```json
{
  "id": "d8f8ad1ce3d015b8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291235,
  "host_pid": "9e6742732c60:1",
  "hash": "9df654d556cb2a0a8d1ed373817643b3784b78d61455d6b1b14fc78b11b54a7c",
  "cid": "QmV19df654d556cb2a0a8d1ed373817643b3784b78d6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291235,
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
      "evaluated_at": 1760291235
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
  "sig": "6e6e7d1f917a092b3ed2e50a17311010054d7dc9cda74daec97211dbf5ee349a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462094881
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 170, 'threshold': 50, 'total_amount': 81057700, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 169, 'first_seen': 1760285763, 'matching_hash': '1dac8a668721a731'}}}