```json
{
  "id": "d61f3d9b783c954f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291485,
  "host_pid": "9e6742732c60:1",
  "hash": "95a840b7c6a5969209f76504b2b652cdeaa2470b26122c33db1da3b979a6cacf",
  "cid": "QmV195a840b7c6a5969209f76504b2b652cdeaa2470b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291485,
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
      "evaluated_at": 1760291485
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
  "sig": "0e079f636b5e14d5a3166110c76de1693dfe0bbe59130976dd42716cbbd89e10"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279745557
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 176, 'threshold': 50, 'total_amount': 16478176, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 175, 'first_seen': 1760285765, 'matching_hash': '46b84f4cf2bc4bde'}}}