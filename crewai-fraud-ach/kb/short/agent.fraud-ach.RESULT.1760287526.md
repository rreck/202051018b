```json
{
  "id": "8ad49d962dd19752",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287526,
  "host_pid": "9e6742732c60:1",
  "hash": "411cac31652e4ae772257cca0841e882d5585134d4c37021e6d5bd42363cc495",
  "cid": "QmV1411cac31652e4ae772257cca0841e882d5585134",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287526,
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
      "evaluated_at": 1760287526
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
  "sig": "c019429514bf09d02988ddf93678e5dbc1fc4ab9dd178ca33e716a73767429c6"
}
```

Fraud detected: amount_anomaly (score: 73)
Transaction: 063100272253110
Details: {'velocity': {'fraud_detected': True, 'risk_score': 76, 'details': {'transaction_count': 63, 'threshold': 50, 'total_amount': 434163807, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 62, 'first_seen': 1760285764, 'matching_hash': 'c9de6cf87e9b501f'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6891489}}}