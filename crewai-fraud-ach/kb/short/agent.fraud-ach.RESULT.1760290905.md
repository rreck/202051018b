```json
{
  "id": "777ded34dd9e33f3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290905,
  "host_pid": "9e6742732c60:1",
  "hash": "056fac1a308e4de9ada5e08c7c3fd9a37580d2207b746ef6aef70d7fede9015d",
  "cid": "QmV1056fac1a308e4de9ada5e08c7c3fd9a37580d220",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290905,
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
      "evaluated_at": 1760290905
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
  "sig": "02635dba0ac2394c6ccaab73193cb802fd9e7131f13bbdc342a2cb7e58452f5d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248509249
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 162, 'threshold': 50, 'total_amount': 26658072, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 161, 'first_seen': 1760285764, 'matching_hash': '3102d5e76c589166'}}}