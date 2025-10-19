```json
{
  "id": "996eb74dcdb04819",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294220,
  "host_pid": "9e6742732c60:1",
  "hash": "dacb206707f977703c88aa5bd68f0609f92be607d8eabc8c447d3a03627328d6",
  "cid": "QmV1dacb206707f977703c88aa5bd68f0609f92be607",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294220,
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
      "evaluated_at": 1760294220
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
  "sig": "99221cfc403354a4362313d74e3562946024dddaf17d1dcb14ecfa3fbb607094"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462101683
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 77611014, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285763, 'matching_hash': 'e66600e2d7fa312e'}}}maly': {'fraud_detected': True, 'risk_score': 79, 'details': {'zscore': 3.97, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 7694908}}}