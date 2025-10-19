```json
{
  "id": "802b5f8c086b7533",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288476,
  "host_pid": "9e6742732c60:1",
  "hash": "4066d69b2c54cb90a6dbdc05986b1355db0524cd68accb44666f90e8ef67fad0",
  "cid": "QmV14066d69b2c54cb90a6dbdc05986b1355db0524cd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288476,
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
      "evaluated_at": 1760288476
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
  "sig": "1d05e8c33a512a3c901b46d899eedaabe91e7387278b7254bf85bfb1f1b91676"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598844081
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 94, 'threshold': 50, 'total_amount': 18514992, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 93, 'first_seen': 1760285765, 'matching_hash': 'ecb0c176cd8f032c'}}}