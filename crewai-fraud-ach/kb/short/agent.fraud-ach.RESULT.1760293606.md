```json
{
  "id": "e217186c43636e1d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293606,
  "host_pid": "9e6742732c60:1",
  "hash": "71e68bfbe8f4c29326bfcfba707b94717f6590fbbf9dc3abf3cf7b0a04dc9faa",
  "cid": "QmV171e68bfbe8f4c29326bfcfba707b94717f6590fb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293606,
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
      "evaluated_at": 1760293606
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
  "sig": "0b52a8c9b994f928511613eebdab402d43bada4021b43cc00e49ba95e7c0a992"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 026009594828050
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 222, 'threshold': 50, 'total_amount': 222000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 221, 'first_seen': 1760285763, 'matching_hash': '3e77f188c48013ab'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}