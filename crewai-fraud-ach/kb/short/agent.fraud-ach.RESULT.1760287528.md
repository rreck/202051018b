```json
{
  "id": "fa0765f520d12713",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287528,
  "host_pid": "9e6742732c60:1",
  "hash": "b922728af8c9759ba51c53f7c817854aff4b6f024618c63098e44b757afad0f8",
  "cid": "QmV1b922728af8c9759ba51c53f7c817854aff4b6f02",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287528,
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
      "evaluated_at": 1760287528
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
  "sig": "4475851af5b92c58184a20cf9da33e1271529e3b2e9f321ab659de041d64259c"
}
```

Fraud detected: amount_anomaly (score: 73)
Transaction: 021000024248654
Details: {'velocity': {'fraud_detected': True, 'risk_score': 76, 'details': {'transaction_count': 63, 'threshold': 50, 'total_amount': 488498787, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 62, 'first_seen': 1760285765, 'matching_hash': '6adb7b11c0829b91'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 7753949}}}