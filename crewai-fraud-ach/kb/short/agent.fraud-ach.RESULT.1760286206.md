```json
{
  "id": "37e1d21a7422eaaf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286206,
  "host_pid": "9e6742732c60:1",
  "hash": "8acbbae3a7fc72c1f8f91116d8eae97da7a89c39a52dc1425c8ba24972ad5837",
  "cid": "QmV18acbbae3a7fc72c1f8f91116d8eae97da7a89c39",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286206,
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
      "evaluated_at": 1760286206
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
  "sig": "9cd0d1c77f711d752c16b4ba5ec84f93cba7f45f820b69d814fee8035be673f6"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 021000021703881
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 116377560, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 17, 'first_seen': 1760285763, 'matching_hash': '20cca8b4db3b5ffd'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6465420}}}