```json
{
  "id": "b16a37cd89a87eb0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288295,
  "host_pid": "9e6742732c60:1",
  "hash": "2fd8a96b0a91e1cad7a4b34c835c0f71bf0167e66330e9edd2d4731405d435fe",
  "cid": "QmV12fd8a96b0a91e1cad7a4b34c835c0f71bf0167e6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288295,
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
      "evaluated_at": 1760288295
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
  "sig": "71037ffe2668a5da49e859d2522337bb8bc47ad318d360aaa915b381a9ac1a26"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 021000029533260
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 89, 'threshold': 50, 'total_amount': 713650861, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 88, 'first_seen': 1760285763, 'matching_hash': '6cc2b71c57585513'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 8018549}}}