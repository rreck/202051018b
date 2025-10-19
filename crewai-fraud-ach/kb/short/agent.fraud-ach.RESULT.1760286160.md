```json
{
  "id": "13d6b6fcd5724244",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286160,
  "host_pid": "9e6742732c60:1",
  "hash": "775ed32f0efb590015e9fc7f7521945db35bc14e617248fd4bd0a38f93c35174",
  "cid": "QmV1775ed32f0efb590015e9fc7f7521945db35bc14e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286160,
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
      "evaluated_at": 1760286160
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
  "sig": "a1fc69bd1a8f6a97adcdc4f04972d621b89ddf5761ffbfdd0c4191c89c296e7f"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 121000242463666
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 125044528, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 15, 'first_seen': 1760285764, 'matching_hash': '3cd63f27035973d0'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 7815283}}}