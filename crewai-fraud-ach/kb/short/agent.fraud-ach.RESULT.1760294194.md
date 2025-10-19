```json
{
  "id": "08331b485c187668",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294194,
  "host_pid": "9e6742732c60:1",
  "hash": "76097e531ac4199c3faf737025f769d0c42e18cfd487d1ac8b11fd1c98d0e558",
  "cid": "QmV176097e531ac4199c3faf737025f769d0c42e18cf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294194,
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
      "evaluated_at": 1760294194
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
  "sig": "9ed71101b1bcfa9c582133e02058787ed2708e3ee5aa5cf560131a6eda1d1ee5"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 122105156669076
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 233000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760285763, 'matching_hash': '4057ff9fca3d2276'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}