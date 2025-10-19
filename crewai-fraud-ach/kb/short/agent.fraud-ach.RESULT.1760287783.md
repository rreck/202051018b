```json
{
  "id": "7e1cab9498ffb5c8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287783,
  "host_pid": "9e6742732c60:1",
  "hash": "a0f3317020e0f9fe131313d12751a0c537d31a8f63f02fcc737872405d07cd54",
  "cid": "QmV1a0f3317020e0f9fe131313d12751a0c537d31a8f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287783,
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
      "evaluated_at": 1760287783
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
  "sig": "92fbc9a5bf62a4ae53886919c9180fc4575d0015f60278da7c4bfb14fbb64dca"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153716353
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 148, 'threshold': 50, 'total_amount': 23459924, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 147, 'first_seen': 1760284979, 'matching_hash': '4e18e54a79e9d8ab'}}}mount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}