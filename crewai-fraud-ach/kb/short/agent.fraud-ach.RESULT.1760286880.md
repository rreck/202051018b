```json
{
  "id": "ac5f2870ebc0ffc7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286880,
  "host_pid": "9e6742732c60:1",
  "hash": "3f2ec295f964bbb5823439094ca83daf6af084d444f6c0bf2381e870a3d52855",
  "cid": "QmV13f2ec295f964bbb5823439094ca83daf6af084d4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286880,
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
      "evaluated_at": 1760286880
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
  "sig": "06056381dc9aebbb96e612052d83d401ae9801ec535ce9174b27de34d108fd44"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 111000025312922
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 229991040, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 39, 'first_seen': 1760285765, 'matching_hash': 'ec5c02804d9cd63b'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 5749776}}}