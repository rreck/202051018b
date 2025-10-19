```json
{
  "id": "951e9cb606f0c38c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286648,
  "host_pid": "9e6742732c60:1",
  "hash": "b6d6e0815956955be94edb27eb8865e53d8eb58a21b91211ba9d1c1ecee0c3ba",
  "cid": "QmV1b6d6e0815956955be94edb27eb8865e53d8eb58a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286648,
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
      "evaluated_at": 1760286648
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "af1acd66a1c5df405241557d7ef7dc5039184702cdca9f495598104eca27843c"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000024109289
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11179808, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 31, 'first_seen': 1760285765, 'matching_hash': 'ac2c8f9ff893d8ff'}}}