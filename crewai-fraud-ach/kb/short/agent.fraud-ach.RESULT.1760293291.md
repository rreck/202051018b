```json
{
  "id": "d91dfd4a3c9990fb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293291,
  "host_pid": "9e6742732c60:1",
  "hash": "41dd9e97fc9607cb2987ed555c52964f46d7eed58f8eb8a5916a7a9d4b182204",
  "cid": "QmV141dd9e97fc9607cb2987ed555c52964f46d7eed5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293291,
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
      "evaluated_at": 1760293291
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
  "sig": "fed9f7cea8b37fd75d053271aab06c040c462d06d4b1d78780597a03c9c1d597"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274578801
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 215, 'threshold': 50, 'total_amount': 37762600, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 214, 'first_seen': 1760285765, 'matching_hash': 'c58645b7bcecdbfd'}}}