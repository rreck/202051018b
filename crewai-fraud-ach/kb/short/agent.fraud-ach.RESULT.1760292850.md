```json
{
  "id": "d349f8d19db46191",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292850,
  "host_pid": "9e6742732c60:1",
  "hash": "c32d07265408fa9d9f0b0c3229eb06e6f990f44b0ae7904529047f9bd88db84f",
  "cid": "QmV1c32d07265408fa9d9f0b0c3229eb06e6f990f44b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292850,
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
      "evaluated_at": 1760292850
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
  "sig": "05a14dd0d178af230b1d7a168510bdd0befb049c263d4bcda7a31f41bf6e2c15"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022841229
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 206, 'threshold': 50, 'total_amount': 36701990, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 205, 'first_seen': 1760285763, 'matching_hash': '5d206cfe266207b6'}}}