```json
{
  "id": "de9e5a3ba95b37da",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289828,
  "host_pid": "9e6742732c60:1",
  "hash": "783923c176f7b3a5e91189a9f4b565f8ff1cfb5d1f5a97970d78192bea7b0102",
  "cid": "QmV1783923c176f7b3a5e91189a9f4b565f8ff1cfb5d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289828,
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
      "evaluated_at": 1760289828
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
  "sig": "d496967f00311105c19c0ca674aa881ba90574520dc546f9a770e0ba96fa3912"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025341279
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 134, 'threshold': 50, 'total_amount': 55120230, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 133, 'first_seen': 1760285763, 'matching_hash': 'e2ff1695635a899d'}}}