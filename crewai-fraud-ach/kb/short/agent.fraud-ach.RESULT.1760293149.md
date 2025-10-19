```json
{
  "id": "64ca3c13ea8c7c51",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293149,
  "host_pid": "9e6742732c60:1",
  "hash": "99d513cc45a3047f6e447561ddb168f0e8ea5e679e8b40b43d316d4d3fbe9c53",
  "cid": "QmV199d513cc45a3047f6e447561ddb168f0e8ea5e67",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293149,
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
      "evaluated_at": 1760293149
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
  "sig": "34aeb948e7fa3bf1afa5008d71541e9de591942bc6ccb33f227162eb5052975c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039867307
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 212, 'threshold': 50, 'total_amount': 14523908, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 211, 'first_seen': 1760285765, 'matching_hash': '2a6987d2199b8b86'}}}