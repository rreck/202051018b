```json
{
  "id": "3238bbb644de3d4e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291052,
  "host_pid": "9e6742732c60:1",
  "hash": "9e4f36a2c5a40e1d1c188c10e95988d19b0af3614f893d3c5384ab12203457a5",
  "cid": "QmV19e4f36a2c5a40e1d1c188c10e95988d19b0af361",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291052,
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
      "evaluated_at": 1760291052
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
  "sig": "cebff61e0aa02e27c2c2e93a4bdd882fc102885dadb547d17127fc34d6582b65"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000035430614
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 166, 'threshold': 50, 'total_amount': 48391988, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 165, 'first_seen': 1760285763, 'matching_hash': '12aaf4f6bb764c37'}}}