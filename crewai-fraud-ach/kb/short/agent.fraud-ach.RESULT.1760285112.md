```json
{
  "id": "8ab14fa8c2fc122f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285112,
  "host_pid": "9e6742732c60:1",
  "hash": "086e09e31a6f0bc6f5636ffaa086bea7b793a7e74eff6fe8cfc2e96a970c5ba6",
  "cid": "QmV1086e09e31a6f0bc6f5636ffaa086bea7b793a7e7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285112,
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
      "evaluated_at": 1760285112
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
  "sig": "9051ce4581fd4b1cf287e07e1dd274b43f60d5b0fedad6017c998e0f59acf458"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000247969582
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 13, 'first_seen': 1760284979, 'matching_hash': '259c183eb9552f9c'}}}