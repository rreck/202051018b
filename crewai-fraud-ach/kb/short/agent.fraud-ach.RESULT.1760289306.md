```json
{
  "id": "1d00cf7e5383e592",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289306,
  "host_pid": "9e6742732c60:1",
  "hash": "3dbe7dcfd81e66641177ce49a1bdb1cf82e102b0a658544f52b61f9a3a0305e2",
  "cid": "QmV13dbe7dcfd81e66641177ce49a1bdb1cf82e102b0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289306,
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
      "evaluated_at": 1760289306
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
  "sig": "1022bf7383f12f895688447d97e6b96990c71bb720c2dbf9829f9f465edbbfc7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274571178
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 119, 'threshold': 50, 'total_amount': 56638883, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 118, 'first_seen': 1760285765, 'matching_hash': '2fe0a786c074c752'}}}