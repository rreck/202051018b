```json
{
  "id": "d4f7e16d81b25b1f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288980,
  "host_pid": "9e6742732c60:1",
  "hash": "e378bf9d670ebb210b35d67f0af77f1061bcfdbaab80e4b308b238a5c7bc9ded",
  "cid": "QmV1e378bf9d670ebb210b35d67f0af77f1061bcfdba",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288980,
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
      "evaluated_at": 1760288980
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
  "sig": "77cd8f3f98c12cdfdcb4163ef0df207e2d93ecb62093edbb10c4d533ca046f74"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158500131
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 110, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 109, 'first_seen': 1760285763, 'matching_hash': 'd40f962f80a48e01'}}}een': 1760285763, 'matching_hash': 'f9baa0480a932ad2'}}}maly': {'fraud_detected': True, 'risk_score': 90, 'details': {'zscore': 5.08, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9655961}}}