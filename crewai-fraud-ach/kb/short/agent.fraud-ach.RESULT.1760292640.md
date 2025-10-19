```json
{
  "id": "b24b8e18e781f1b5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292640,
  "host_pid": "9e6742732c60:1",
  "hash": "754ef4369649da763070be45f45a7eb712037a4fea89e3aba0ba190b2d6e4d4f",
  "cid": "QmV1754ef4369649da763070be45f45a7eb712037a4f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292640,
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
      "evaluated_at": 1760292641
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
  "sig": "45f4289114a4be9f0c0cc4730c617be5be5e4398c54401ca03f80bf2f28b1b47"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242172457
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 202, 'threshold': 50, 'total_amount': 95176340, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 201, 'first_seen': 1760285763, 'matching_hash': '180325de6151a8c9'}}}