```json
{
  "id": "1ac6ef1ed4b6158a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287517,
  "host_pid": "9e6742732c60:1",
  "hash": "c6cdaca63f94a822a8f2a17df02582e075dab414fd81466f38e49286f3bca398",
  "cid": "QmV1c6cdaca63f94a822a8f2a17df02582e075dab414",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287517,
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
      "evaluated_at": 1760287517
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
  "sig": "df33959911ecce9db344b480cf001d539e463ece772cd525ca5f9f3e9cbc4068"
}
```

Fraud detected: amount_anomaly (score: 73)
Transaction: 031201465557479
Details: {'velocity': {'fraud_detected': True, 'risk_score': 76, 'details': {'transaction_count': 63, 'threshold': 50, 'total_amount': 419942880, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 62, 'first_seen': 1760285764, 'matching_hash': '962c9a9fec8a4a1a'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6665760}}}ksum'}}}