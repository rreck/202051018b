```json
{
  "id": "c40b6445bb1faafc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285893,
  "host_pid": "9e6742732c60:1",
  "hash": "dd2a0f845471192ba3f9be47a490dc61c35b8e6bd50b1508163325be47ff9b96",
  "cid": "QmV1dd2a0f845471192ba3f9be47a490dc61c35b8e6b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285893,
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
      "evaluated_at": 1760285893
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
  "sig": "22ff3371aad4c995cf2f00c0e908ccd9c4b4d32a4b80804d9e9f7f4e7893850c"
}
```

Fraud detected: amount_anomaly (score: 75)
Transaction: 026009592955504
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 59844988, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 6, 'first_seen': 1760285765, 'matching_hash': 'e4b1ef1aea3a67a1'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 71, 'details': {'zscore': 3.2, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 8549284}}}