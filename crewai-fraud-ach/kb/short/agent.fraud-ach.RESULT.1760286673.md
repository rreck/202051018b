```json
{
  "id": "3f6490e6ad68a920",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286673,
  "host_pid": "9e6742732c60:1",
  "hash": "5ff32d618ed5b3c2e6f84bca13b2e02affad162633b1094bca3e468545fdee3f",
  "cid": "QmV15ff32d618ed5b3c2e6f84bca13b2e02affad1626",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286673,
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
      "evaluated_at": 1760286673
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
  "sig": "235cd2775f4ec09f8e83fd2171eeda989d3624510c6656b72830d5b0fe980fcd"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201462554282
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 32, 'first_seen': 1760285763, 'matching_hash': '2083692f538c0312'}}}