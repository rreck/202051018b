```json
{
  "id": "b21efc3544a3935c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285031,
  "host_pid": "9e6742732c60:1",
  "hash": "89de2ca092786765ac0b8f9543c2e737808a5bbfbc1ef9182342467ed1aae306",
  "cid": "QmV189de2ca092786765ac0b8f9543c2e737808a5bbf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285031,
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
      "evaluated_at": 1760285031
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
  "sig": "2fd1c20a0fdfb7dd015f10e2a946b26c346c6931b8cc0fd9813f7f50b6a15142"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000026203898
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 5, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}