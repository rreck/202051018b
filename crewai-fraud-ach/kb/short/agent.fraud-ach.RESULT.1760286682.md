```json
{
  "id": "64dd0029c4c9ffa0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286682,
  "host_pid": "9e6742732c60:1",
  "hash": "5e856e19c22fa81ff070edb4fe1df9f2193006787228421d16385f0fcc6f3d5f",
  "cid": "QmV15e856e19c22fa81ff070edb4fe1df9f219300678",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286682,
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
      "evaluated_at": 1760286682
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
  "sig": "d0263ab4e65492498e399c29a2fb5a45ce9406af020c5b01164464b469be359f"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10502184, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 32, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}