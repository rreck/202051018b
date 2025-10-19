```json
{
  "id": "d42c7e6edc37d759",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287134,
  "host_pid": "9e6742732c60:1",
  "hash": "867b7e6a0326582b848ae2ef9e9a6e2abca160b7c6032600fb46275c132e11f2",
  "cid": "QmV1867b7e6a0326582b848ae2ef9e9a6e2abca160b7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287134,
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
      "evaluated_at": 1760287134
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
  "sig": "d405f70f99d1df09ef08478173520221883ae3dd93c3fa110b0cf5b92a9c3ca1"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 121000240089409
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 300812470, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 48, 'first_seen': 1760285765, 'matching_hash': 'a79d0bf31de09717'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6139030}}}