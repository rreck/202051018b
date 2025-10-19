```json
{
  "id": "c6753cea447f249f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289366,
  "host_pid": "9e6742732c60:1",
  "hash": "2eb2ffeb4c020a8b3e244213e5e3e52710aad365f8979b781274aa26458cf91a",
  "cid": "QmV12eb2ffeb4c020a8b3e244213e5e3e52710aad365",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289366,
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
      "evaluated_at": 1760289366
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
  "sig": "558889af37323cee8d162f9b5f1989ff85b1ef17b31edde7872b0188597de0af"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272268645
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 121, 'threshold': 50, 'total_amount': 53277631, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 120, 'first_seen': 1760285765, 'matching_hash': '088fbc730f5432fe'}}}