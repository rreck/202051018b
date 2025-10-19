```json
{
  "id": "8e858e948fc4a705",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290322,
  "host_pid": "9e6742732c60:1",
  "hash": "baa7b70b632e827a1370dc89ee5a8c90048c0c0d85ba89f127c4e1a809908a31",
  "cid": "QmV1baa7b70b632e827a1370dc89ee5a8c90048c0c0d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290322,
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
      "evaluated_at": 1760290322
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
  "sig": "e30dba3ab1a8c172f9ee6f9070aaeb1a10f65f6c91617e755dbb46d2cf8dec6d"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 122105156669076
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 147, 'threshold': 50, 'total_amount': 147000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 146, 'first_seen': 1760285763, 'matching_hash': '4057ff9fca3d2276'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}