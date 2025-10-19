```json
{
  "id": "dd00371684194202",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293807,
  "host_pid": "9e6742732c60:1",
  "hash": "77d27bbc73a0413f4c20866c0aa0e5f54c7a249ce85934893247a6faaffcb724",
  "cid": "QmV177d27bbc73a0413f4c20866c0aa0e5f54c7a249c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293807,
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
      "evaluated_at": 1760293808
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
  "sig": "eba96256079b74cc93e3f434f0b7a1b627893a31f5a1aedf9a8468770fdd88f2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271403003
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 56500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285763, 'matching_hash': 'a8be718158b742cd'}}}