```json
{
  "id": "b96868430a2edb20",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286532,
  "host_pid": "9e6742732c60:1",
  "hash": "1c20de7fc6a678412dd064df3ec259d2184f2ea199ebcca646fc165554e84a7c",
  "cid": "QmV11c20de7fc6a678412dd064df3ec259d2184f2ea1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286532,
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
      "evaluated_at": 1760286532
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "83127ad1138494acecc501546fa803fb791b3663717626ec23a7079828de6a76"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201460625527
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 13444760, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 27, 'first_seen': 1760285765, 'matching_hash': 'd2e448c8360c8b26'}}}