```json
{
  "id": "9b8206c108da89ac",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287348,
  "host_pid": "9e6742732c60:1",
  "hash": "0ddba7d8cf2ac1372f256addfd432eb03442a72dbf525e30831c6b38a91f2198",
  "cid": "QmV10ddba7d8cf2ac1372f256addfd432eb03442a72d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287348,
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
      "evaluated_at": 1760287348
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
  "sig": "369a30d3024f96bdd61c80c23d46f43c706711fb69c32281b3593ff4a6731f01"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 122105155084324
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 57, 'threshold': 50, 'total_amount': 391896432, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 56, 'first_seen': 1760285763, 'matching_hash': '91e9478c27780a65'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6875376}}}ksum'}}}