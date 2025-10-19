```json
{
  "id": "faecda2f55f54ce7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286057,
  "host_pid": "9e6742732c60:1",
  "hash": "5dc764e6d700eb644e697aeb3c103b70ff814b1e6ffdeddddb7f10c878272c17",
  "cid": "QmV15dc764e6d700eb644e697aeb3c103b70ff814b1e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286057,
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
      "evaluated_at": 1760286057
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
  "sig": "e98e2c0cef1548ea189e63a1fe59c9a146259e071c0b4aedcfb7a33180539027"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 122105158843417
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 102105705, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 12, 'first_seen': 1760285763, 'matching_hash': '108807581913276f'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 7854285}}}