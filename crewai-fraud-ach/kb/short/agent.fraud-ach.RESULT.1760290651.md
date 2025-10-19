```json
{
  "id": "e9d6ad55d524ca40",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290651,
  "host_pid": "9e6742732c60:1",
  "hash": "d90291b9b05ccadece0e1473a7423477b348b29aaaa458489537b1ee2705d673",
  "cid": "QmV1d90291b9b05ccadece0e1473a7423477b348b29a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290651,
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
      "evaluated_at": 1760290651
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
  "sig": "282f23bec58c6abad5b69e9017aa9d03ad892cedbe5e9d18befb686279018239"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272156319
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 156, 'threshold': 50, 'total_amount': 11993904, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 155, 'first_seen': 1760285763, 'matching_hash': '6d26908715188c7a'}}}