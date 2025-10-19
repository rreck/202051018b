```json
{
  "id": "2e83b6d670503241",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285978,
  "host_pid": "9e6742732c60:1",
  "hash": "69bc8e8a4f83012adb6c56fdfa91719e370f0a0ecd74be39f719b39fcdd12b94",
  "cid": "QmV169bc8e8a4f83012adb6c56fdfa91719e370f0a0e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285978,
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
      "evaluated_at": 1760285978
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
  "sig": "df9c46df624f1cd06500508914443de834addb5dbc60c14ee9aa49c5ea094dc7"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100274472610
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 9, 'first_seen': 1760285764, 'matching_hash': '7db40904e20d1f88'}}}