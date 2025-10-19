```json
{
  "id": "0630387ab410c7ed",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291751,
  "host_pid": "9e6742732c60:1",
  "hash": "cb5869abb48930c2af7d43b9ef37bb8927ac692145048b5d8a6b841f2927f390",
  "cid": "QmV1cb5869abb48930c2af7d43b9ef37bb8927ac6921",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291751,
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
      "evaluated_at": 1760291751
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
  "sig": "1ee35e9c385776945023db3b072b7bdb2af729661117cd8bb86969b44933ccf5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594714846
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 258, 'threshold': 50, 'total_amount': 127979868, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 257, 'first_seen': 1760284979, 'matching_hash': 'bc3982de93079c96'}}}