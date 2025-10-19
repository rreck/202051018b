```json
{
  "id": "1720224832d1f5fe",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288467,
  "host_pid": "9e6742732c60:1",
  "hash": "8ce3f1c3b54b3a896b8ad6df53d4678bb39d3558975a680da872b2618eb3b601",
  "cid": "QmV18ce3f1c3b54b3a896b8ad6df53d4678bb39d3558",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288467,
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
      "evaluated_at": 1760288467
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
  "sig": "c0d1a66cfa439da44fe7e236e5d21b829d6a3870692fc8c10d9e564d4783896a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271369125
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 94, 'threshold': 50, 'total_amount': 14556746, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 93, 'first_seen': 1760285763, 'matching_hash': 'b975113295de86ab'}}}