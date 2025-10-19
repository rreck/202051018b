```json
{
  "id": "921aa566d2654196",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291670,
  "host_pid": "9e6742732c60:1",
  "hash": "518854528088f60bec37f77eeb77b53e2e56b4f29d11cea0baf837d022c215dc",
  "cid": "QmV1518854528088f60bec37f77eeb77b53e2e56b4f2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291670,
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
      "evaluated_at": 1760291670
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
  "sig": "52a07c224fa8b40d46afc0ce5f41d096e80b30c8ab9af5f6a092fbfa09b76ece"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 031201467949832
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 180, 'threshold': 50, 'total_amount': 180000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 179, 'first_seen': 1760285764, 'matching_hash': '3eb2ce6b003836d6'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}