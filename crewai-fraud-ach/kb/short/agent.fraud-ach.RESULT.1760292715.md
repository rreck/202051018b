```json
{
  "id": "3535f594b4ac21b3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292715,
  "host_pid": "9e6742732c60:1",
  "hash": "8cf636f2ed59e7ac66787af9709592c0cb7b228abc5d36e6bfe9f6f5222e26de",
  "cid": "QmV18cf636f2ed59e7ac66787af9709592c0cb7b228a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292715,
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
      "evaluated_at": 1760292715
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
  "sig": "57fad07c25b747fd2d92751631332e7d669b8ca24f18f9c869341fc2d76323b3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021517830
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 203, 'threshold': 50, 'total_amount': 60429649, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 202, 'first_seen': 1760285765, 'matching_hash': '323b6ce2946b0561'}}}