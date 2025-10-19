```json
{
  "id": "e0a9ac18719f98dc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286011,
  "host_pid": "9e6742732c60:1",
  "hash": "95047b76f4764809aea3d1ea2b62c5e9a81831658574f5d3eac056e0dae8ecb0",
  "cid": "QmV195047b76f4764809aea3d1ea2b62c5e9a8183165",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286011,
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
      "evaluated_at": 1760286011
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
  "sig": "137c594e22f1b36ae8b311e68347f4f247a0663d8dae0200f88373f9f58ffdd6"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 031201467009203
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 87271492, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 10, 'first_seen': 1760285765, 'matching_hash': 'e7911512dd8ff7c4'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 7933772}}}