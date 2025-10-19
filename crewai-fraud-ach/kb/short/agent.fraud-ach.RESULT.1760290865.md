```json
{
  "id": "9efc5b6cfc436b1c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290865,
  "host_pid": "9e6742732c60:1",
  "hash": "fe526e398147d0d147e4ea10ee713cfd78f17746d44b2537b0146646bdcf23d2",
  "cid": "QmV1fe526e398147d0d147e4ea10ee713cfd78f17746",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290865,
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
      "evaluated_at": 1760290865
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
  "sig": "c45dadc470cade1437123ac9605debdce869f49c561d52b2550142699c894c01"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100277826130
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 161, 'threshold': 50, 'total_amount': 10082464, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 160, 'first_seen': 1760285764, 'matching_hash': '6123129413abd06e'}}}