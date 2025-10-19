```json
{
  "id": "f3bea3bed2286795",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291292,
  "host_pid": "9e6742732c60:1",
  "hash": "0f5cd671aad595e61319c694208b5432420f8e84e749e14e4a79e1c6b3c8c6fa",
  "cid": "QmV10f5cd671aad595e61319c694208b5432420f8e84",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291292,
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
      "evaluated_at": 1760291292
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
  "sig": "302af9fdc439f49a771f93ae7ef74f56c54353add73578cede3159c4a6dea90a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025329406
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 171, 'threshold': 50, 'total_amount': 82819917, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 170, 'first_seen': 1760285765, 'matching_hash': '4bb9b304f38123bb'}}}