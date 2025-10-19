```json
{
  "id": "39ed52fa90293919",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291536,
  "host_pid": "9e6742732c60:1",
  "hash": "072900c012d5e8929435060bb18a417e4d6b093c5f10d852f8d20879eb9f079b",
  "cid": "QmV1072900c012d5e8929435060bb18a417e4d6b093c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291536,
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
      "evaluated_at": 1760291537
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
  "sig": "08fdfe43875bf31f82d938a5449f0518d860bfe7176475d0a9b082379785d6cd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249454336
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 177, 'threshold': 50, 'total_amount': 26286093, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 176, 'first_seen': 1760285763, 'matching_hash': '6b4cd9d1923f5d4e'}}}}