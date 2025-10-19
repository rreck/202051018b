```json
{
  "id": "0294aa780fec1c36",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292470,
  "host_pid": "9e6742732c60:1",
  "hash": "16556116efb927c1131041b16ca21430e19345f27f9d5c66dc35dbed6e2d5262",
  "cid": "QmV116556116efb927c1131041b16ca21430e19345f2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292470,
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
      "evaluated_at": 1760292470
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
  "sig": "cf0bdede76c4f2c4b41522dfa5b93adc8f4e794ebdd8a3c170d198924ab37774"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276148173
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 198, 'threshold': 50, 'total_amount': 55973610, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 197, 'first_seen': 1760285765, 'matching_hash': 'f15677eba424e05f'}}}