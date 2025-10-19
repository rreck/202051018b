```json
{
  "id": "3b09d5e110737ff3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292937,
  "host_pid": "9e6742732c60:1",
  "hash": "94879738a9014a3764b4385dcf07f17256f982fe1f8faad66a65727390a4fcfa",
  "cid": "QmV194879738a9014a3764b4385dcf07f17256f982fe",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292937,
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
      "evaluated_at": 1760292937
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
  "sig": "860ff7c00a1be0318b8680e8bf26827f513e7780e976fff7321f65ee627f6621"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270162443
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 208, 'threshold': 50, 'total_amount': 103382656, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 207, 'first_seen': 1760285763, 'matching_hash': 'e637274c2d5e4084'}}}