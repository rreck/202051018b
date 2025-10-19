```json
{
  "id": "c1d1dd939fc4f82e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293969,
  "host_pid": "9e6742732c60:1",
  "hash": "a1e82d51e14031869d185d828ac3afd0cb5f1a886dea5d0c3f49a77c004e520d",
  "cid": "QmV1a1e82d51e14031869d185d828ac3afd0cb5f1a88",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293969,
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
      "evaluated_at": 1760293969
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
  "sig": "313f8a9b0984747f5ba96f79f4f0fa885dd09d14ef237578d7513a7dc27e15f6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244210031
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 93303531, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760285764, 'matching_hash': '572834c9990ead18'}}}