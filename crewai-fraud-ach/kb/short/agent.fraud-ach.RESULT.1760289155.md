```json
{
  "id": "2aeb9e2636902cee",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289155,
  "host_pid": "9e6742732c60:1",
  "hash": "613d15f5ff389b4cfabd7b6500b8bb22b8b10405bef25d199d91c622ad4fb3bf",
  "cid": "QmV1613d15f5ff389b4cfabd7b6500b8bb22b8b10405",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289155,
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
      "evaluated_at": 1760289155
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
  "sig": "21cdb440b9dd0e484364221c3b2c70e1aeabfe6d7c635f72f46f55445439dc03"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465580268
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 115, 'threshold': 50, 'total_amount': 36334135, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 114, 'first_seen': 1760285764, 'matching_hash': 'af9caaaec8320bfb'}}}