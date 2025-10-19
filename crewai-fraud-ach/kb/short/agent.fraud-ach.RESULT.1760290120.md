```json
{
  "id": "64fce07c1e6ac292",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290120,
  "host_pid": "9e6742732c60:1",
  "hash": "b9c404a8c3f3c4acb1a021802dd9f5b2b096cf592ccea752e7279461eb27b156",
  "cid": "QmV1b9c404a8c3f3c4acb1a021802dd9f5b2b096cf59",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290120,
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
      "evaluated_at": 1760290120
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
  "sig": "2c0b8d78846b364b3bf2b137ba5ae38cd56e44e3f49ab50692c6f1251df39086"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023603818
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 142, 'threshold': 50, 'total_amount': 63761692, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 141, 'first_seen': 1760285764, 'matching_hash': '07334b550f79eb68'}}}