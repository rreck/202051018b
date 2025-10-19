```json
{
  "id": "5fb0a4f92e29d7e0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287011,
  "host_pid": "9e6742732c60:1",
  "hash": "4cff9086f84576c6095281ab99909b6d85cebbcf50ff9f8cd7a704e313d67e18",
  "cid": "QmV14cff9086f84576c6095281ab99909b6d85cebbcf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287011,
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
      "evaluated_at": 1760287011
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "946265f202507119ccc9686b9719428ae19cb54b56877468c03aef22e0cfc7a9"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201462273667
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 20091915, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 44, 'first_seen': 1760285763, 'matching_hash': 'db56bbc4ded669a9'}}}