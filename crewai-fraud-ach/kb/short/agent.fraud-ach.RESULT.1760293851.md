```json
{
  "id": "43c9a8ecad84ef3e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293851,
  "host_pid": "9e6742732c60:1",
  "hash": "39f19ed778a8a95f248cc06ddff1e31fb516b1d71e87539e9016c5234aacda0d",
  "cid": "QmV139f19ed778a8a95f248cc06ddff1e31fb516b1d7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293851,
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
      "evaluated_at": 1760293851
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
  "sig": "a01c2dc63199478e97c815f66e05ec41d02ec525a9db47a142bfc44b8e2fd6b4"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 063100279773830
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 113500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285763, 'matching_hash': '49e9eab15cee1f0f'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}