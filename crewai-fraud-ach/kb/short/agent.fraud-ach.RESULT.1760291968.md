```json
{
  "id": "f0827bc1f41f9591",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291968,
  "host_pid": "9e6742732c60:1",
  "hash": "a874ebea7de043e7df8a8573c949efbea813802deb075982089a245aed7c7a0c",
  "cid": "QmV1a874ebea7de043e7df8a8573c949efbea813802d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291968,
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
      "evaluated_at": 1760291968
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
  "sig": "555051e358467494343e9e16ec272e95bcd898d9479173f8cfaa4651dd395484"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598660548
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 187, 'threshold': 50, 'total_amount': 42996723, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 186, 'first_seen': 1760285763, 'matching_hash': '4ba6ddd8e6715c89'}}}maly': {'fraud_detected': True, 'risk_score': 79, 'details': {'zscore': 4.0, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7743228}}}