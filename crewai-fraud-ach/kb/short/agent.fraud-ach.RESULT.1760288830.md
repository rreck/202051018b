```json
{
  "id": "2ea6b3f84dd36c83",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288830,
  "host_pid": "9e6742732c60:1",
  "hash": "b23a6c2318c6a19ac1ac2638e99087fb3d938842e7667f59b6af3bc050887eb0",
  "cid": "QmV1b23a6c2318c6a19ac1ac2638e99087fb3d938842",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288830,
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
      "evaluated_at": 1760288830
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "d7eb68a24277c25d314d3e361771ec51ddb314bfa3f443a9c1c64deb4eaa8f55"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469103825
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 105, 'threshold': 50, 'total_amount': 37987845, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 104, 'first_seen': 1760285764, 'matching_hash': 'e83bf56ea8077a45'}}}