```json
{
  "id": "c3eaa381eb315d59",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293626,
  "host_pid": "9e6742732c60:1",
  "hash": "6eb159f43b0d391038f52741d395b8fa1d71f43ca8a90aeebae0f873f0f158a7",
  "cid": "QmV16eb159f43b0d391038f52741d395b8fa1d71f43c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293626,
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
      "evaluated_at": 1760293626
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
  "sig": "c864cdfd3c0aa8fc48131a73b0a7627f59ed00426907c0bc1ea013f0111b6037"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000035599822
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 222, 'threshold': 50, 'total_amount': 34247274, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 221, 'first_seen': 1760285763, 'matching_hash': 'a98e7fc79b0958d1'}}}