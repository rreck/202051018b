```json
{
  "id": "b619c4f75786f78e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294562,
  "host_pid": "9e6742732c60:1",
  "hash": "dc130ab6915caa082a9c136010dbde0e05d464f0716f46e41b95a9e4176b686f",
  "cid": "QmV1dc130ab6915caa082a9c136010dbde0e05d464f0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294562,
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
      "evaluated_at": 1760294562
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
  "sig": "1c20d6d6b006cb86166b2bca0d21a425cd443f472a5676266e393ece9d33763a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158912506
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 36926640, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285765, 'matching_hash': 'bcd6f6796bd6b696'}}}