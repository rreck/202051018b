```json
{
  "id": "f56583272f42e854",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294179,
  "host_pid": "9e6742732c60:1",
  "hash": "e0d26c896dfc54bd6f2419ff1ad7eda73984df52cfeb0d8c94c1a3c73984c2a0",
  "cid": "QmV1e0d26c896dfc54bd6f2419ff1ad7eda73984df52",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294179,
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
      "evaluated_at": 1760294179
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
  "sig": "275a8c04860ddaba78b7cf3726bbe4299c79a6e50016921dd96950d4b31d7f87"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031437397
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 111132379, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760285764, 'matching_hash': 'dcc4ccfc6ce6722f'}}}