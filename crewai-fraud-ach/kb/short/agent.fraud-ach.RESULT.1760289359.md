```json
{
  "id": "8f2414abd8525156",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289359,
  "host_pid": "9e6742732c60:1",
  "hash": "2bf992de30b5647f43b0fe1c21bb1eb7c14f0f1955bf96a187d2eb09d586780b",
  "cid": "QmV12bf992de30b5647f43b0fe1c21bb1eb7c14f0f19",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289359,
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
      "evaluated_at": 1760289359
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
  "sig": "a9be81f1995fff5f1c34d8f1e0ebe5a2aae37332f9ea308de23ce461bb0692f2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464554990
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 121, 'threshold': 50, 'total_amount': 33046673, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 120, 'first_seen': 1760285763, 'matching_hash': 'ab9afd20a22fc7b8'}}}