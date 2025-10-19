```json
{
  "id": "6b71f3584f734143",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289990,
  "host_pid": "9e6742732c60:1",
  "hash": "5216a90a4af3bdcffeef45ea542a72a79ecc6d732254f6d64b16d7e401f8e9c3",
  "cid": "QmV15216a90a4af3bdcffeef45ea542a72a79ecc6d73",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289990,
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
      "evaluated_at": 1760289990
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
  "sig": "6521c52890822fa7ff93d897efc5fa865f6000557e0a13d86fb1dd5ff5b7bca8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 138, 'threshold': 50, 'total_amount': 43918224, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 137, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}