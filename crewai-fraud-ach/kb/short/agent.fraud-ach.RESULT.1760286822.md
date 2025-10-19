```json
{
  "id": "2ee75349c16e0928",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286822,
  "host_pid": "9e6742732c60:1",
  "hash": "4acef37c8d9f18d6e1c953d0f4881cfdac58d5f0e0a68a209c0a93270ed98b5e",
  "cid": "QmV14acef37c8d9f18d6e1c953d0f4881cfdac58d5f0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286822,
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
      "evaluated_at": 1760286822
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
  "sig": "929ab6f568ffba67f854cc981fdfe7895aac4bd787a5a19d42842b6910bfb975"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105157659459
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 13828618, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 37, 'first_seen': 1760285765, 'matching_hash': 'b2c549e42e296c8f'}}}