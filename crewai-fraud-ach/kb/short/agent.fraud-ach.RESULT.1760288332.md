```json
{
  "id": "2939333d6f31911d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288332,
  "host_pid": "9e6742732c60:1",
  "hash": "9b4816dda5856278bf0624b06c1349889d605b36e2badf91ec696ed65f0da685",
  "cid": "QmV19b4816dda5856278bf0624b06c1349889d605b36",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288332,
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
      "evaluated_at": 1760288332
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
  "sig": "27b956672a62b25f575750ee8f3c861b94914d717f6cf709b208a9f35c5fde51"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031437397
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 90, 'threshold': 50, 'total_amount': 42926670, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 89, 'first_seen': 1760285764, 'matching_hash': 'dcc4ccfc6ce6722f'}}}