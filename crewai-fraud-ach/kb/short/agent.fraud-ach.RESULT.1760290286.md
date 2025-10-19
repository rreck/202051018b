```json
{
  "id": "f6565342490d6f11",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290286,
  "host_pid": "9e6742732c60:1",
  "hash": "f4f9959555f5189534a8ca6cf210fd688795d025ba0c7efbc29d539fd0e0c9fc",
  "cid": "QmV1f4f9959555f5189534a8ca6cf210fd688795d025",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290286,
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
      "evaluated_at": 1760290286
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
  "sig": "bff3d9af93fc4329c0767770299939ac55219295694e74b7b558a103aeb50067"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270344488
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 146, 'threshold': 50, 'total_amount': 38945938, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 145, 'first_seen': 1760285764, 'matching_hash': 'ec3de169da630728'}}}