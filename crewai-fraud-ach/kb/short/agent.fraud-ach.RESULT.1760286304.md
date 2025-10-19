```json
{
  "id": "c4a8d2fc98f1bfb5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286304,
  "host_pid": "9e6742732c60:1",
  "hash": "47b10c6309250ea5c7c2d3b81ef6c91038d2990dbbd1dd7e8226378c6f2df082",
  "cid": "QmV147b10c6309250ea5c7c2d3b81ef6c91038d2990d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286304,
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
      "evaluated_at": 1760286304
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
  "sig": "5b065f442bc0da6fd6d6cba60c6246ddc0c14a2a8f9a7a045e1ca411ab6a60bd"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009596556765
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 20, 'first_seen': 1760285763, 'matching_hash': '746e82f5d57aeb25'}}}