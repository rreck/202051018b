```json
{
  "id": "4e762c81b217cf4b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285764,
  "host_pid": "9e6742732c60:1",
  "hash": "025fe79f0b406401f70ccbe38108efe434afe95b353ddb0853a2731f43924c5e",
  "cid": "QmV1025fe79f0b406401f70ccbe38108efe434afe95b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285764,
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
      "evaluated_at": 1760285764
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
  "sig": "253cb75349b7a8ba5883e26eaa09e791cb6b8ed1d06c8de118ac5531139c0f96"
}
```

Fraud detected: amount_anomaly (score: 60)
Transaction: 031201467532863
Details: {'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 5514339}}}