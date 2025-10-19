```json
{
  "id": "1314e7fa2c72f085",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289405,
  "host_pid": "9e6742732c60:1",
  "hash": "0feef377292a07f4dc404d5190ffbac46422a8f5bfdff21fd188bd7dfd5f5a6d",
  "cid": "QmV10feef377292a07f4dc404d5190ffbac46422a8f5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289405,
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
      "evaluated_at": 1760289405
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
  "sig": "6dbbc36d4b7f04dcde25e966b31715ab392a1aba92224c5b97a9ea7e236c6072"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462554282
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 122, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 121, 'first_seen': 1760285763, 'matching_hash': '2083692f538c0312'}}}