```json
{
  "id": "e80f4a6923175cac",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290914,
  "host_pid": "9e6742732c60:1",
  "hash": "03575b06c28df406a0be04f082ef3a7296b6429955b3b9947bdee22b267159f2",
  "cid": "QmV103575b06c28df406a0be04f082ef3a7296b64299",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290914,
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
      "evaluated_at": 1760290914
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
  "sig": "c5179c203cefcac5c678d2b67482768aabc89088528878f1513f04b7c1a5c4da"
}
```

Fraud detected: amount_anomaly (score: 88)
Transaction: 121000242463666
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 162, 'threshold': 50, 'total_amount': 1266075846, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 161, 'first_seen': 1760285764, 'matching_hash': '3cd63f27035973d0'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 80, 'details': {'zscore': 4.04, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7815283}}}