```json
{
  "id": "bbc99d624cecb6c0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290519,
  "host_pid": "9e6742732c60:1",
  "hash": "5af3377f98c0567061e72ec9988b3cc467821d61a08aaa4f65067db043735f16",
  "cid": "QmV15af3377f98c0567061e72ec9988b3cc467821d61",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290519,
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
      "evaluated_at": 1760290519
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
  "sig": "850f2985de0dc46d85735364bc2c2635c045d7b2aab5fc45a9014394fad046a5"
}
```

Fraud detected: amount_anomaly (score: 86)
Transaction: 026009595707011
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 152, 'threshold': 50, 'total_amount': 1046613024, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 151, 'first_seen': 1760285765, 'matching_hash': 'bce5819bd1402454'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.51, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6885612}}}