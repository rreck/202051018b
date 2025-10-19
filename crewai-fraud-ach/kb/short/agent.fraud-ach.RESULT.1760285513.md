```json
{
  "id": "136231aeabb17027",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285513,
  "host_pid": "9e6742732c60:1",
  "hash": "0779b96518fe0cea101c66ab53bd5d7cdc513717f1cd556256fc97558710b8e2",
  "cid": "QmV10779b96518fe0cea101c66ab53bd5d7cdc513717",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285513,
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
      "evaluated_at": 1760285513
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_high"
  ],
  "sig": "15cf01f768fd6e22bc86b7f2f05cb63dcacc248cb0af2b99173ad3827bbae99a"
}
```

Fraud detected: amount_anomaly (score: 77)
Transaction: 021000029388663
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 53, 'threshold': 50, 'total_amount': 519162030, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 52, 'first_seen': 1760284979, 'matching_hash': '503d742180c16441'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 77, 'details': {'zscore': 3.75, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9795510}}}