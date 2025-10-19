```json
{
  "id": "c61cebc463c47ceb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293585,
  "host_pid": "9e6742732c60:1",
  "hash": "3bbe561758bafaaa8d6680a75bec3c95f59196758310eb9564e32a0e56e1eb05",
  "cid": "QmV13bbe561758bafaaa8d6680a75bec3c95f5919675",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293585,
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
      "evaluated_at": 1760293585
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
  "sig": "fdf60f8ad0bf52e8b6de561ff0a8daa23e72d2dae56d3ddce0347606b2ccb285"
}
```

Fraud detected: amount_anomaly (score: 87)
Transaction: 063100278543685
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 1566748118, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285765, 'matching_hash': 'e9470cd0cc07fb40'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 76, 'details': {'zscore': 3.62, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 7089358}}}