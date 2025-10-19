```json
{
  "id": "a227f62b6c6c5a78",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290503,
  "host_pid": "9e6742732c60:1",
  "hash": "0eb09306d69ea28057229936121d7a9316571635a266f146c03662322ebae2af",
  "cid": "QmV10eb09306d69ea28057229936121d7a9316571635",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290503,
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
      "evaluated_at": 1760290504
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
  "sig": "800cf8f1e5d4de8f725c7d8f2975565279920ffe8e7cf9e8f777e54495d53c19"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026701294
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 152, 'threshold': 50, 'total_amount': 39163256, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 151, 'first_seen': 1760285764, 'matching_hash': 'c6488d75609f0f90'}}}