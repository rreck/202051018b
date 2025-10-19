```json
{
  "id": "4abbc8b24b975a6c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286347,
  "host_pid": "9e6742732c60:1",
  "hash": "1bfc9110ddab6b795c701fea60daca3f526c293295ac31974cfe196065fdbd6a",
  "cid": "QmV11bfc9110ddab6b795c701fea60daca3f526c2932",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286347,
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
      "evaluated_at": 1760286347
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
  "sig": "d25f19c729acf78c480fa315801c52407e81645cbb2956eb1f2ea5b4487325ae"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000243232456
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 21, 'first_seen': 1760285765, 'matching_hash': '1b0a7dc1f650d378'}}}