```json
{
  "id": "5e6ada45cfec7d19",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287619,
  "host_pid": "9e6742732c60:1",
  "hash": "c55336bca6165c2d7c49d9e6d0db41a6dd657bd7663ca4ca958666402cf4878a",
  "cid": "QmV1c55336bca6165c2d7c49d9e6d0db41a6dd657bd7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287619,
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
      "evaluated_at": 1760287619
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
  "sig": "23a8bcfb821e83c5e55ae6a1c7353c97e9d3fe7b4e82ab9b9cb011eaf51d4be0"
}
```

Fraud detected: duplicate_transaction (score: 83)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 82, 'details': {'transaction_count': 66, 'threshold': 50, 'total_amount': 21004368, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 65, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}