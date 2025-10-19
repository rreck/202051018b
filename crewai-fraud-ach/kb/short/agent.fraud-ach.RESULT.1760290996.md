```json
{
  "id": "2b43479342d7cf9f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290996,
  "host_pid": "9e6742732c60:1",
  "hash": "6cb94e82fd11619292d2c60133b708940bfb1d0095d2c0670cbd73ed79b35bda",
  "cid": "QmV16cb94e82fd11619292d2c60133b708940bfb1d00",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290996,
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
      "evaluated_at": 1760290996
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
  "sig": "0e21bb2b54037d581797c3fdfa51733c03497282a4dd4b2a9dc3325b3d715e84"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150676701
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 164, 'threshold': 50, 'total_amount': 77204968, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 163, 'first_seen': 1760285765, 'matching_hash': 'f947c72340b5e951'}}}