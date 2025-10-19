```json
{
  "id": "fb43f17c6def51ef",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292282,
  "host_pid": "9e6742732c60:1",
  "hash": "3453cf42e58083302e85674e912d8f9b8d7dbd9c61c64704267830c67904ae1a",
  "cid": "QmV13453cf42e58083302e85674e912d8f9b8d7dbd9c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292282,
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
      "evaluated_at": 1760292282
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
  "sig": "56239f26307088f0c1581c1aa0752eb232f08cf5b8699ed744187832f9ce490b"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 063100275692414
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 194, 'threshold': 50, 'total_amount': 1069543922, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 193, 'first_seen': 1760285764, 'matching_hash': '9e6182bea86cf2e1'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 5513113}}}