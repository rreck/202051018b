```json
{
  "id": "e9df7562a8a3b9ce",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286606,
  "host_pid": "9e6742732c60:1",
  "hash": "fa552fd8d3748552f0577faa9cfe719f57cd592a2979817b85de31246835c440",
  "cid": "QmV1fa552fd8d3748552f0577faa9cfe719f57cd592a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286606,
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
      "evaluated_at": 1760286606
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
  "sig": "79e69f6e525741d96079366a580d16db02701764fa39b5ee3acca32f85e0a15f"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009593787585
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 13454155, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 30, 'first_seen': 1760285763, 'matching_hash': '27c7bfe810f6d733'}}}