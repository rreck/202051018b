```json
{
  "id": "76f4a3525e668b4c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288862,
  "host_pid": "9e6742732c60:1",
  "hash": "a752b2666946bd8a0b211706697a45c196139f393401a283bea6db86cfc128fd",
  "cid": "QmV1a752b2666946bd8a0b211706697a45c196139f39",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288862,
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
      "evaluated_at": 1760288862
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
  "sig": "e68400788831effae77d3588e41006bef3ebfff9607e0917f993307a8092ac0e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031910208
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 106, 'threshold': 50, 'total_amount': 40407412, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 105, 'first_seen': 1760285763, 'matching_hash': '8397d9ba38a9dfb7'}}}