```json
{
  "id": "77419ac78da7e1cd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291658,
  "host_pid": "9e6742732c60:1",
  "hash": "7873bb401c082bac3fe5f1caaffc6145ae0c9785d9bcd08c9ea68ea1c5f6b04d",
  "cid": "QmV17873bb401c082bac3fe5f1caaffc6145ae0c9785",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291658,
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
      "evaluated_at": 1760291658
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
  "sig": "6049e9189b6c25bef356418708919ecd4e51e951e05c1be0a9d5dffba056866c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009595557022
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 180, 'threshold': 50, 'total_amount': 85676580, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 179, 'first_seen': 1760285764, 'matching_hash': '3443c05f2ecc9733'}}}