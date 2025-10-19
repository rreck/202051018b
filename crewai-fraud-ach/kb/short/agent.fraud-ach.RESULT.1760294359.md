```json
{
  "id": "aa1f234ce5ddf156",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294359,
  "host_pid": "9e6742732c60:1",
  "hash": "4bc9d5c67e67429037d8df9572ceafb6dc9b2906d393547a442b7936838b476c",
  "cid": "QmV14bc9d5c67e67429037d8df9572ceafb6dc9b2906",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294359,
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
      "evaluated_at": 1760294359
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
  "sig": "81a124215105c372b8d83f49f1d9d51dbe896e35d06470362007ee9ea33139c5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157659459
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 85882996, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285765, 'matching_hash': 'b2c549e42e296c8f'}}}