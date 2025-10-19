```json
{
  "id": "638c9bd3e8bd32d4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293135,
  "host_pid": "9e6742732c60:1",
  "hash": "62d976a9ed44dc8fb2c42124453d01f1b70a979e8a7cca705063762411f2212d",
  "cid": "QmV162d976a9ed44dc8fb2c42124453d01f1b70a979e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293135,
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
      "evaluated_at": 1760293135
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
  "sig": "db4994392e3c2e10b94a23800dd0c543b7d46aad0a974fd4f85e9eaa71a73f28"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594714846
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 288, 'threshold': 50, 'total_amount': 142861248, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 287, 'first_seen': 1760284979, 'matching_hash': 'bc3982de93079c96'}}}