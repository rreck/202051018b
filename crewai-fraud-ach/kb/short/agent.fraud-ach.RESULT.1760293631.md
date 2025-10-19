```json
{
  "id": "eb0a9d22a0722fda",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293631,
  "host_pid": "9e6742732c60:1",
  "hash": "54a14f99c31e615d7f60fbe7e0860cc663ff80f24b451924985ed629bb065c20",
  "cid": "QmV154a14f99c31e615d7f60fbe7e0860cc663ff80f2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293631,
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
      "evaluated_at": 1760293631
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
  "sig": "01c27073126e06b6abbf594f781bcf7ad1120bc7365cf446ab1a5f21e886e403"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 031201467949832
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 222, 'threshold': 50, 'total_amount': 222000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 221, 'first_seen': 1760285764, 'matching_hash': '3eb2ce6b003836d6'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}