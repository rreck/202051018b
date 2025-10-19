```json
{
  "id": "9e6d4dc9119bf704",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292597,
  "host_pid": "9e6742732c60:1",
  "hash": "ca649f8811e0ed1ee01d2b32f92aa4c8076628c21f45795c4249a0cfdc9f4988",
  "cid": "QmV1ca649f8811e0ed1ee01d2b32f92aa4c8076628c2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292597,
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
      "evaluated_at": 1760292597
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
  "sig": "de5bd3153bcf760ab1a4e148aeb0b8a1f392415539287f588f533dd460701eea"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240515775
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 201, 'threshold': 50, 'total_amount': 47931867, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 200, 'first_seen': 1760285763, 'matching_hash': 'c332d96fce6ec0fa'}}}maly': {'fraud_detected': True, 'risk_score': 72, 'details': {'zscore': 3.3, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6511445}}}