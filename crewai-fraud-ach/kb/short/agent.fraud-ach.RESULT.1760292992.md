```json
{
  "id": "ce4edb5190b6ebf8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292992,
  "host_pid": "9e6742732c60:1",
  "hash": "170fcd1076cb38995f764ab6e3e9d1b5ff3dd661e753e88adab70d5e8f71a26b",
  "cid": "QmV1170fcd1076cb38995f764ab6e3e9d1b5ff3dd661",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292992,
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
      "evaluated_at": 1760292992
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
  "sig": "32530f91ef7bf81506182054be201810f8beba8d3052ea213d194f141aa953f6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025207502
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 209, 'threshold': 50, 'total_amount': 91807848, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 208, 'first_seen': 1760285765, 'matching_hash': 'b87463fc74d5c9ed'}}}