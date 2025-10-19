```json
{
  "id": "78a171427d930192",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291846,
  "host_pid": "9e6742732c60:1",
  "hash": "3eec0c43653a7b4aa58ab3896127590fa32799355ceb4c4e47e4d21767a2e36c",
  "cid": "QmV13eec0c43653a7b4aa58ab3896127590fa3279935",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291846,
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
      "evaluated_at": 1760291846
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
  "sig": "18daa1ce864f4321431545d660c1f5ed6ff887213fa2e9220f46433499f96d32"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 026009591978167
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 184, 'threshold': 50, 'total_amount': 184000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 183, 'first_seen': 1760285765, 'matching_hash': '6b05f8817543e1fe'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}