```json
{
  "id": "fc303f71a787c509",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291038,
  "host_pid": "9e6742732c60:1",
  "hash": "34c43d32e88d7f748c28a899837be27c6d0ce6b100ff5ff7796f0412965270bc",
  "cid": "QmV134c43d32e88d7f748c28a899837be27c6d0ce6b1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291038,
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
      "evaluated_at": 1760291038
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
  "sig": "8166c99059590093f06e9d2205cefecd5a75f94cc23bbd369dd5d64d14aa4fcc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021718881
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 165, 'threshold': 50, 'total_amount': 21592395, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 164, 'first_seen': 1760285765, 'matching_hash': 'c5f4c03352e0db07'}}}