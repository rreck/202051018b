```json
{
  "id": "ad2d31a4a58f9f62",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288801,
  "host_pid": "9e6742732c60:1",
  "hash": "8ef9028d1dd1ef11a219f4bfb1fe6abaf1c3dfe1f5f2ea6276690293f608aaba",
  "cid": "QmV18ef9028d1dd1ef11a219f4bfb1fe6abaf1c3dfe1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288801,
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
      "evaluated_at": 1760288801
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
  "sig": "609445996288f7f48282a0dc9664a8256f5f49b1a2d41500ebfd2d88a0c7fe0b"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 021000023602502
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 104, 'threshold': 50, 'total_amount': 104000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 103, 'first_seen': 1760285765, 'matching_hash': 'eacad8d3d1630a37'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}