```json
{
  "id": "ec90bf44b45ed239",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288995,
  "host_pid": "9e6742732c60:1",
  "hash": "2178097c274f09804b3c035cf23e7f7ade672d7cc0158ec55170c1ce1b52b2bd",
  "cid": "QmV12178097c274f09804b3c035cf23e7f7ade672d7c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288995,
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
      "evaluated_at": 1760288995
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
  "sig": "97770805e2f93aacf3dfccd5bfd057596fd4aca29e8891e82b4bf3c2a276b8cf"
}
```

Fraud detected: amount_anomaly (score: 90)
Transaction: 044000033143138
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 110, 'threshold': 50, 'total_amount': 979128810, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 109, 'first_seen': 1760285764, 'matching_hash': '6d0d609b65d243f3'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 86, 'details': {'zscore': 4.65, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8901171}}}