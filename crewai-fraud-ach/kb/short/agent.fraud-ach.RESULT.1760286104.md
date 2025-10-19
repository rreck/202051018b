```json
{
  "id": "a567df79f4571429",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286104,
  "host_pid": "9e6742732c60:1",
  "hash": "c614ac1a3210d54074b46df814a1191960709f35059ccf3c3ec763c662078b4b",
  "cid": "QmV1c614ac1a3210d54074b46df814a1191960709f35",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286104,
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
      "evaluated_at": 1760286104
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
  "sig": "a5020674cca15242086f9713b39246ac13bf3345795b2977381daa4189724d62"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105153543170
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 13, 'first_seen': 1760285765, 'matching_hash': 'bc1f881c41cfe07c'}}}