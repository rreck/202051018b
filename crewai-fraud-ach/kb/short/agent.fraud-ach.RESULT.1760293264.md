```json
{
  "id": "685d6838b28c377e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293264,
  "host_pid": "9e6742732c60:1",
  "hash": "490961d9ca4ddfb3a3158f80cd04f539ffc5e49a43a59277f8b9dc15538d7ace",
  "cid": "QmV1490961d9ca4ddfb3a3158f80cd04f539ffc5e49a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293264,
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
      "evaluated_at": 1760293264
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
  "sig": "e73b74b762ff9e9bf2038a2d34e11301724e03a4eefa547fff8dba8e743e4fb9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150315138
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 215, 'threshold': 50, 'total_amount': 74129850, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 214, 'first_seen': 1760285763, 'matching_hash': '420167e0317803c0'}}}