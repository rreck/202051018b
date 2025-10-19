```json
{
  "id": "4ee4b482d421b74d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290175,
  "host_pid": "9e6742732c60:1",
  "hash": "542f101d9f6c5a9f072bc0f19f8a5c28701578f878d8bf22403ac39db754e0d2",
  "cid": "QmV1542f101d9f6c5a9f072bc0f19f8a5c28701578f8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290175,
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
      "evaluated_at": 1760290175
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
  "sig": "df8d2c7cc8ea895b9f7bf98faa58aec83f0cab0e6ab971c729f2f4bffbb5a57e"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 021000023602502
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 143, 'threshold': 50, 'total_amount': 143000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 142, 'first_seen': 1760285765, 'matching_hash': 'eacad8d3d1630a37'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}