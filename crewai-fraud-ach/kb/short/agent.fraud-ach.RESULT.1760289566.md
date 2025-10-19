```json
{
  "id": "b1e80e234f7414c6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289566,
  "host_pid": "9e6742732c60:1",
  "hash": "129ee1184aa66262424bf950deda7a2394c92a4a2c3486fe9aef7b5d25f08603",
  "cid": "QmV1129ee1184aa66262424bf950deda7a2394c92a4a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289566,
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
      "evaluated_at": 1760289566
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
  "sig": "df3756ddca881f1054de15dc0644227a000bf0feb765295afb65bacfad733c1f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278631812
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 127, 'threshold': 50, 'total_amount': 24107394, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 126, 'first_seen': 1760285763, 'matching_hash': 'e154fa328ed40444'}}}