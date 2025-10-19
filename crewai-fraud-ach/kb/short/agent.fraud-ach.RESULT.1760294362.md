```json
{
  "id": "d703656df57005f3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294362,
  "host_pid": "9e6742732c60:1",
  "hash": "2e195d0736e271043f54eeb523ea85a972f47c9b7a2b026f2f7b043972591209",
  "cid": "QmV12e195d0736e271043f54eeb523ea85a972f47c9b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294362,
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
      "evaluated_at": 1760294362
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
  "sig": "9f9941443b771d5a79cf060f1bb7c9d30e613d96cad75a47096d8707ee87cf39"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598844081
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 46484448, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285765, 'matching_hash': 'ecb0c176cd8f032c'}}}