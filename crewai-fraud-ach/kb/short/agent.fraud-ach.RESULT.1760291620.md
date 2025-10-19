```json
{
  "id": "f2d285e892854c0e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291620,
  "host_pid": "9e6742732c60:1",
  "hash": "639b91870f69f7199635309a6d9f6c73b09a181107365aa6318816e130251bfb",
  "cid": "QmV1639b91870f69f7199635309a6d9f6c73b09a1811",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291620,
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
      "evaluated_at": 1760291620
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
  "sig": "9bc788ede31d587b6eeec65955c92b3b284279486e8493c0e2ef85a9339572bf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464924143
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 255, 'threshold': 50, 'total_amount': 103628175, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 254, 'first_seen': 1760284979, 'matching_hash': '7b94effc1b7c4489'}}}