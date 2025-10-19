```json
{
  "id": "ab9af034f53a38da",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286674,
  "host_pid": "9e6742732c60:1",
  "hash": "fc276f6f49b887d26d3cfacaa1472a3ed47e63421ee55d98325bae2aed45080a",
  "cid": "QmV1fc276f6f49b887d26d3cfacaa1472a3ed47e6342",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286674,
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
      "evaluated_at": 1760286674
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
  "sig": "8951f7df24c7e8dd9ec87eb667f07ecaa2ec45e3b344a697ad2c7de6f09e616f"
}
```

Fraud detected: round_amount_pattern (score: 65)
Transaction: 031201467949832
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 33000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 32, 'first_seen': 1760285764, 'matching_hash': '3eb2ce6b003836d6'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}