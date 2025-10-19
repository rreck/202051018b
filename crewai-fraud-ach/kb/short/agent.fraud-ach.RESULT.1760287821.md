```json
{
  "id": "2dadf22a2bc9d539",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287821,
  "host_pid": "9e6742732c60:1",
  "hash": "90d0999a6b4ce9807ada11bdc8225f0f89244653f2a71efd0827bb089877aac5",
  "cid": "QmV190d0999a6b4ce9807ada11bdc8225f0f89244653",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287821,
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
      "evaluated_at": 1760287821
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
  "sig": "5c5a8be99367ec1b5b71cf63876843beb979e7713a09b40f436f5d68a9474f37"
}
```

Fraud detected: duplicate_transaction (score: 90)
Transaction: 121000247383202
Details: {'velocity': {'fraud_detected': True, 'risk_score': 96, 'details': {'transaction_count': 73, 'threshold': 50, 'total_amount': 29072615, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 72, 'first_seen': 1760285765, 'matching_hash': '32929947211460fd'}}}