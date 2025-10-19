```json
{
  "id": "878ee2b1e5a6c5ca",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289782,
  "host_pid": "9e6742732c60:1",
  "hash": "2c44761cf9d3c4d373b407346d032d9947531e39474281c7f547089b57d7a602",
  "cid": "QmV12c44761cf9d3c4d373b407346d032d9947531e39",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289782,
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
      "evaluated_at": 1760289782
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
  "sig": "b182405d2fbc93e1447479316e0ec297181c691d3e2d3a7847e96fc65877137e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151297418
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 133, 'threshold': 50, 'total_amount': 58037609, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 132, 'first_seen': 1760285763, 'matching_hash': '6f92d94cce52eccd'}}}