```json
{
  "id": "9049824ff2bf4caa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293830,
  "host_pid": "9e6742732c60:1",
  "hash": "5d31e09f1c7fc9aa6f7dbe25280f0067d03db1d9ebc4ff4bce32f1c8327eb8a1",
  "cid": "QmV15d31e09f1c7fc9aa6f7dbe25280f0067d03db1d9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293830,
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
      "evaluated_at": 1760293830
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "71b7d8b41588574ea3d97158d3de5e2eb82ac872806321e34b1b3d15a22ee1f7"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 122105156669076
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 226000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285763, 'matching_hash': '4057ff9fca3d2276'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}