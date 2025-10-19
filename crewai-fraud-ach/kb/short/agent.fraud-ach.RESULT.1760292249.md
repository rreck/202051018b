```json
{
  "id": "46e017584f76ec50",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292249,
  "host_pid": "9e6742732c60:1",
  "hash": "76ffaa13be93e8cebbd9fd7e946c8187e50d84c26c0fd32d90e76fbd6303872e",
  "cid": "QmV176ffaa13be93e8cebbd9fd7e946c8187e50d84c2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292249,
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
      "evaluated_at": 1760292249
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
  "sig": "e09b800ad869496b13c2234c6d49258725bd01a073b66140f4f32ac962b5a0da"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022109746
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 193, 'threshold': 50, 'total_amount': 23262097, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 192, 'first_seen': 1760285765, 'matching_hash': '2a578690bb80e431'}}}