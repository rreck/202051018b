```json
{
  "id": "d8b828fa4be654f3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287206,
  "host_pid": "9e6742732c60:1",
  "hash": "9c0ee96c874644a17e4ed3d72a22a17f7299af779063194be06cafc4ad4da11c",
  "cid": "QmV19c0ee96c874644a17e4ed3d72a22a17f7299af77",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287206,
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
      "evaluated_at": 1760287206
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
  "sig": "ba069f965f147fb9c91103611fc9ba574fbe7891faf9703a8bb207bdfaf0ed46"
}
```

Fraud detected: amount_anomaly (score: 77)
Transaction: 021000021072241
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 52, 'threshold': 50, 'total_amount': 502109972, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 51, 'first_seen': 1760285763, 'matching_hash': 'ac02650f27bf80d6'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 76, 'details': {'zscore': 3.69, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9655961}}}