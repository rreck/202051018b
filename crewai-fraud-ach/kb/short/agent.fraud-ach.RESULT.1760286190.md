```json
{
  "id": "8c69d02490fcc070",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286190,
  "host_pid": "9e6742732c60:1",
  "hash": "b0d80eed52dc7d0594f2a4e07c91b9cefe054eaf4e7eb1aebc80d25a511584b6",
  "cid": "QmV1b0d80eed52dc7d0594f2a4e07c91b9cefe054eaf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286190,
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
      "evaluated_at": 1760286190
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
  "sig": "678c2b3e63af5c95e5d45db4f74bc3220d6191a17e9a700eff99487260205e10"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 031201464331888
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 107657039, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 16, 'first_seen': 1760285764, 'matching_hash': '6a7d940bcd4512ca'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6332767}}}