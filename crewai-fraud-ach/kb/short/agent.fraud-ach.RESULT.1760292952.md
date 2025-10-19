```json
{
  "id": "a18922ad2a2c2072",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292952,
  "host_pid": "9e6742732c60:1",
  "hash": "b950d634d338ecb254e5b61c4a4abbe9eed48a6b50e0ee50e4080ad5e446408d",
  "cid": "QmV1b950d634d338ecb254e5b61c4a4abbe9eed48a6b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292952,
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
      "evaluated_at": 1760292952
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
  "sig": "ad3d5db79b68c9edcc1a7cfbb7582a402b36a69a4908c7edb51979ee728dcb2b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274578801
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 208, 'threshold': 50, 'total_amount': 36533120, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 207, 'first_seen': 1760285765, 'matching_hash': 'c58645b7bcecdbfd'}}}