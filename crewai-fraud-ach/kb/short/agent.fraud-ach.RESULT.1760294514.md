```json
{
  "id": "efb4cdc27af246eb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294514,
  "host_pid": "9e6742732c60:1",
  "hash": "f7507c527870371dd3f888efea59dd632ab87f55dd67766c1491f0cf8d382ca5",
  "cid": "QmV1f7507c527870371dd3f888efea59dd632ab87f55",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294514,
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
      "evaluated_at": 1760294514
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
  "sig": "2055e99482c571c2ee0d9eecba8714044171899b549324860c5e629168c742c2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000036717829
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 41284621, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285764, 'matching_hash': '49d069f76f563267'}}}