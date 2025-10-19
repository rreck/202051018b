```json
{
  "id": "9be9a4276ee3fd63",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289547,
  "host_pid": "9e6742732c60:1",
  "hash": "c09539095b812b272e3284532a76bf0e33383828b3b927fef8a3326119ba5d6f",
  "cid": "QmV1c09539095b812b272e3284532a76bf0e33383828",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289547,
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
      "evaluated_at": 1760289547
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
  "sig": "88bd3d05e9cd0f890fe8db97d8a6713f9ef092aaf8a92dead9c905751f891311"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460501611
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 126, 'threshold': 50, 'total_amount': 21370986, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 125, 'first_seen': 1760285764, 'matching_hash': 'a26573d157351ea4'}}}