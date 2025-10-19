```json
{
  "id": "7417f37847d7b0bf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290418,
  "host_pid": "9e6742732c60:1",
  "hash": "2b52d92a58e6da855c9a3c8230055b5506f1ba7024499492c92892cc37179be7",
  "cid": "QmV12b52d92a58e6da855c9a3c8230055b5506f1ba70",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290418,
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
      "evaluated_at": 1760290418
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
  "sig": "d5bd20e5f1ded3aae07ea466d59d08a7e83a2830fcd843b670ea979c4de02de6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592077072
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 150, 'threshold': 50, 'total_amount': 35083350, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 149, 'first_seen': 1760285763, 'matching_hash': '86add4fc1587ca1b'}}}