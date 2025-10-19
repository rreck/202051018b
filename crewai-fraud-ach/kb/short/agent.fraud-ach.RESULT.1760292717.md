```json
{
  "id": "02b1ece8a83d37b0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292717,
  "host_pid": "9e6742732c60:1",
  "hash": "27baca366f89928286dcd0d58e0c7e305ae35ccaaa721d80377c84d5927520a0",
  "cid": "QmV127baca366f89928286dcd0d58e0c7e305ae35cca",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292717,
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
      "evaluated_at": 1760292717
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
  "sig": "8edec8706aa0af1dea9f920f6aa69aa0dc52c914917ab2cbd9e54e6a2a6316ac"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 203, 'threshold': 50, 'total_amount': 64604344, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 202, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}