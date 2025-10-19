```json
{
  "id": "fe8ae70f2a39138e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289502,
  "host_pid": "9e6742732c60:1",
  "hash": "04b67454df3755eb4043602a9f9ec3499f2ff81889374719a984803177913ffa",
  "cid": "QmV104b67454df3755eb4043602a9f9ec3499f2ff818",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289502,
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
      "evaluated_at": 1760289502
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
  "sig": "e90c14584fa07be9e8827aad5f2a37f8ed36026a5f4c2061171dfe470d20b293"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153839048
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 125, 'threshold': 50, 'total_amount': 21737375, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 124, 'first_seen': 1760285764, 'matching_hash': '20b3840d87952e5c'}}}