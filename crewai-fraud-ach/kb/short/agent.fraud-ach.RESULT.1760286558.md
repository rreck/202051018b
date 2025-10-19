```json
{
  "id": "68022a6ebbb9981d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286558,
  "host_pid": "9e6742732c60:1",
  "hash": "95b2a1cffc9b95382317a84cf4c4c29be2829f49b6c6345de93bad8203f7e994",
  "cid": "QmV195b2a1cffc9b95382317a84cf4c4c29be2829f49",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286558,
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
      "evaluated_at": 1760286558
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
  "sig": "7eadf43a4ba5b3073090e2892ec72932f86094c0688d24319f761affec5037e6"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009598542542
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 28, 'first_seen': 1760285764, 'matching_hash': '3cc1c7bbce52acf6'}}}