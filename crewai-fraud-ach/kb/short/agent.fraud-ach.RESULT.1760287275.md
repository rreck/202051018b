```json
{
  "id": "e75248101c7a1e6a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287275,
  "host_pid": "9e6742732c60:1",
  "hash": "0618271a423c3f26cc2fe58df6efc5a275f3ca5232f34fc5ed88192f1bd8f16c",
  "cid": "QmV10618271a423c3f26cc2fe58df6efc5a275f3ca52",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287275,
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
      "evaluated_at": 1760287275
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
  "sig": "55978fef121e397efa6a9b0959022a0478b0deafac1b002724e07c00e810063e"
}
```

Fraud detected: amount_anomaly (score: 75)
Transaction: 026009598348562
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 54, 'threshold': 50, 'total_amount': 452633508, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 53, 'first_seen': 1760285765, 'matching_hash': '08c1aa7df797b6df'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 71, 'details': {'zscore': 3.12, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 8382102}}}