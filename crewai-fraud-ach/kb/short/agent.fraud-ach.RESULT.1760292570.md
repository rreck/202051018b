```json
{
  "id": "f8bd8299c38dcb3f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292570,
  "host_pid": "9e6742732c60:1",
  "hash": "4905bd3f3dd9543e4ed50dd9701571a860c43a863d3855fd2f2131463663b624",
  "cid": "QmV14905bd3f3dd9543e4ed50dd9701571a860c43a86",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292570,
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
      "evaluated_at": 1760292570
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
  "sig": "c4a0009744782d926127f74bc3f1ac8cd9c105fc98f2f1c2a9b3ff00299681f9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031078531
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 200, 'threshold': 50, 'total_amount': 15380600, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 199, 'first_seen': 1760285765, 'matching_hash': '2bea5b783a868e31'}}}