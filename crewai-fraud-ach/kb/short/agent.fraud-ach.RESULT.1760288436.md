```json
{
  "id": "c25a0ca8328081a1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288436,
  "host_pid": "9e6742732c60:1",
  "hash": "a72c3c9f00b17e1c54726d6432c9e4be51214d3a386e1f9ff077bf46e57021fc",
  "cid": "QmV1a72c3c9f00b17e1c54726d6432c9e4be51214d3a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288436,
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
      "evaluated_at": 1760288436
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
  "sig": "7a89e35c1f0e96a94460cebe8b581567a3035387985bedd3daccd5fe57e580ff"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271105789
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 93, 'threshold': 50, 'total_amount': 25212486, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 92, 'first_seen': 1760285764, 'matching_hash': 'b50c8d05dbdb14ee'}}}