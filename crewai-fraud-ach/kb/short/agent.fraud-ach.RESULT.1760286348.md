```json
{
  "id": "5c3a3f9f85aacb5f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286348,
  "host_pid": "9e6742732c60:1",
  "hash": "2870358af0d62dd52b06dc79033f4dd6b9c0ff94c19d1079393748a9a88f9dde",
  "cid": "QmV12870358af0d62dd52b06dc79033f4dd6b9c0ff94",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286348,
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
      "evaluated_at": 1760286348
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
  "sig": "79dc9793c71998185e49253e79f199f046f37fcb3af7baf967789548b1284dd8"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 111000028976117
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 130935706, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 21, 'first_seen': 1760285765, 'matching_hash': 'f0572624c8eaf0e8'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 5951623}}}