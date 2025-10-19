```json
{
  "id": "8872daed5f1198eb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287419,
  "host_pid": "9e6742732c60:1",
  "hash": "108e6ad1f5db80a233390c7609b0937c089df63ea040725310b2235661d5359a",
  "cid": "QmV1108e6ad1f5db80a233390c7609b0937c089df63e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287419,
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
      "evaluated_at": 1760287419
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
  "sig": "4a6382decbc33fc5048caa1429a86851164b6a9565a0780f24261ea0b0cac1db"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 044000039495479
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 59, 'threshold': 50, 'total_amount': 24045096, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 58, 'first_seen': 1760285765, 'matching_hash': 'bbfd7bc59c80a282'}}}