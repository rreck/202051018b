```json
{
  "id": "b2a9962a343aed82",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294764,
  "host_pid": "9e6742732c60:1",
  "hash": "fb4ae9383888b11bcfa7a896b3d557805955eba2fabb321a8f783326445fcd90",
  "cid": "QmV1fb4ae9383888b11bcfa7a896b3d557805955eba2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294764,
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
      "evaluated_at": 1760294764
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
  "sig": "11fb359c16c34f42c4b1687ec460a6c5f911047bc32323814653bba4a2da084f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243431079
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 31682912, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285764, 'matching_hash': '441814efc7e72dab'}}}