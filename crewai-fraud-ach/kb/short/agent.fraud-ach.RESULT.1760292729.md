```json
{
  "id": "f28098db2d16e9db",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292729,
  "host_pid": "9e6742732c60:1",
  "hash": "0059c6ec75df56597ed51f99a2abb646cd8a2ca575197a0c0ecec48c963ef00b",
  "cid": "QmV10059c6ec75df56597ed51f99a2abb646cd8a2ca5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292729,
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
      "evaluated_at": 1760292729
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_critical"
  ],
  "sig": "51046173e72902e4f624eb1a49b7362f3a1de32dc22ad42930ef540442b39485"
}
```

Fraud detected: amount_anomaly (score: 87)
Transaction: 111000024041930
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 204, 'threshold': 50, 'total_amount': 1502629320, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 203, 'first_seen': 1760285763, 'matching_hash': 'd0d1b4b42d54423e'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 77, 'details': {'zscore': 3.78, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 7365830}}}