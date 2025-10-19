```json
{
  "id": "ebf054fa07f1b53e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294814,
  "host_pid": "9e6742732c60:1",
  "hash": "9c966a321209eda6b0857318a823ce9decf8172cdf67fe2b3f6dffc16fdd40e5",
  "cid": "QmV19c966a321209eda6b0857318a823ce9decf8172c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294814,
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
      "evaluated_at": 1760294814
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
  "sig": "577abd3f6055497f3f071fccfb95f6ed08490ae86602e536d71f1c02a50ff253"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000036907843
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 75521740, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285763, 'matching_hash': '5c57e03938e1b0ed'}}}