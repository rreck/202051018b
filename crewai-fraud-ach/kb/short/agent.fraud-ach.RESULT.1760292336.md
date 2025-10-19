```json
{
  "id": "d1f691247c5fde34",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292336,
  "host_pid": "9e6742732c60:1",
  "hash": "3ef6d75464a148104b513622d83c85c156bdec82c92e70800a67c23a2c55aad2",
  "cid": "QmV13ef6d75464a148104b513622d83c85c156bdec82",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292336,
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
      "evaluated_at": 1760292336
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
  "sig": "6d4b72d106d4e1497ec4158636379a6533c8a0fa50474ea58b600df4ee6e1387"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157031776
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 195, 'threshold': 50, 'total_amount': 45239805, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 194, 'first_seen': 1760285763, 'matching_hash': '2e79bf0e4633df5f'}}}