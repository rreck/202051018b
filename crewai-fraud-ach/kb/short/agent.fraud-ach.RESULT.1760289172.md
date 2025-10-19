```json
{
  "id": "26905013b8aa9072",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289172,
  "host_pid": "9e6742732c60:1",
  "hash": "c4a8dcc9f0968b568011246bf6ee1da523eab37f8e0131ab41e30aee242e00a3",
  "cid": "QmV1c4a8dcc9f0968b568011246bf6ee1da523eab37f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289172,
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
      "evaluated_at": 1760289172
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
  "sig": "b285dceecf4709abcad8462008815ea019b377a0b5ac4533f367eef7d36c08b9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 115, 'threshold': 50, 'total_amount': 36598520, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 114, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}