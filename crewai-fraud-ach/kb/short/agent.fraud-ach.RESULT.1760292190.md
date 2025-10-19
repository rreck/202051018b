```json
{
  "id": "4d0ded7e1b2d1620",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292190,
  "host_pid": "9e6742732c60:1",
  "hash": "13d0e4790a1e045493a556d53392a19178dd13894924b6bdb6954a435d0c2e2f",
  "cid": "QmV113d0e4790a1e045493a556d53392a19178dd1389",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292190,
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
      "evaluated_at": 1760292190
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
  "sig": "85f8554ce2c6d776b25a6264abb014b9511ffe078ae34e030f6f6094bb67dbf6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271109324
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 192, 'threshold': 50, 'total_amount': 48000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 191, 'first_seen': 1760285764, 'matching_hash': '28f72b559ab32ea0'}}}