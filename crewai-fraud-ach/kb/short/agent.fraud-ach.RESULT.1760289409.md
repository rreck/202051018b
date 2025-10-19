```json
{
  "id": "5b0770c5bd4f5cf9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289409,
  "host_pid": "9e6742732c60:1",
  "hash": "0a3c8ba551b6f225c006dea5934534b6c51705fcf5655c5cec3febed288b80f3",
  "cid": "QmV10a3c8ba551b6f225c006dea5934534b6c51705fc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289409,
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
      "evaluated_at": 1760289409
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
  "sig": "4577dc9ba119a4491f544df315c03fc5845f605b318d77c7c19dfad7c44a70d0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033751291
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 122, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 121, 'first_seen': 1760285765, 'matching_hash': '04859aaf1143bd8f'}}}