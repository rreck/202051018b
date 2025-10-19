```json
{
  "id": "5e1fd4e4dacaf216",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292281,
  "host_pid": "9e6742732c60:1",
  "hash": "dae3c2f29f449f1a51a96d639a1608d889ff8d7da03807da68f19ff3a994587a",
  "cid": "QmV1dae3c2f29f449f1a51a96d639a1608d889ff8d7d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292281,
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
      "evaluated_at": 1760292281
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
  "sig": "c1c28c91661f0dea4ad62c834397687f43333432a0b37b8991fd92ac4f016a7b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243741176
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 194, 'threshold': 50, 'total_amount': 59037110, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 193, 'first_seen': 1760285763, 'matching_hash': 'e78a513bf0bcec2f'}}}