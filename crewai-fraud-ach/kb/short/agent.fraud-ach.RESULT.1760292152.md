```json
{
  "id": "23e5ff51938b310e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292152,
  "host_pid": "9e6742732c60:1",
  "hash": "4278ee3cfc9ec101aa82de8c50932b64d3ec556c4c3decbe7dc806a0a060ba61",
  "cid": "QmV14278ee3cfc9ec101aa82de8c50932b64d3ec556c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292152,
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
      "evaluated_at": 1760292152
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
  "sig": "a03f87b5aaa78040e28eed0ac42c5837a92d1dd827606a9a782f9b55abdc9376"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026783731
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 191, 'threshold': 50, 'total_amount': 78584276, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 190, 'first_seen': 1760285763, 'matching_hash': 'dea6d8bb62de6c67'}}}