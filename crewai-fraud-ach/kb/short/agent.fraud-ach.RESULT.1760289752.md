```json
{
  "id": "6dfc4c381ecd6d7f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289752,
  "host_pid": "9e6742732c60:1",
  "hash": "f631c457af1a1faff2003847c63fb2963903fbfba0bda6d709cf72847fa87d0c",
  "cid": "QmV1f631c457af1a1faff2003847c63fb2963903fbfb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289752,
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
      "evaluated_at": 1760289752
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
  "sig": "f6e6113db432a60178e33ac9bcd4f3209cf37c25b3233eaa7a7e850c60027f8d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245035140
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 132, 'threshold': 50, 'total_amount': 53464620, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 131, 'first_seen': 1760285763, 'matching_hash': 'af29b59576821758'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '691661790', 'validation_error': 'Invalid routing number checksum'}}}