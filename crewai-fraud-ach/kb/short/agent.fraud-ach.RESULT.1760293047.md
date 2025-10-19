```json
{
  "id": "ad28e03b588819d3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293047,
  "host_pid": "9e6742732c60:1",
  "hash": "6a1a31ff64bf195bfcafac6cd3dea5b83d38f988b3414fd842b7040084ea3334",
  "cid": "QmV16a1a31ff64bf195bfcafac6cd3dea5b83d38f988",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293047,
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
      "evaluated_at": 1760293047
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
  "sig": "cd2e42e488cb252c3fda8bc5b53e79a2086dc4f2b9dd3e7e127c6507b5d7eb67"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245911336
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 210, 'threshold': 50, 'total_amount': 104535060, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 209, 'first_seen': 1760285765, 'matching_hash': '6e0081c3975eda61'}}}