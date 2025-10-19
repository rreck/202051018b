```json
{
  "id": "fab33be370696422",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293750,
  "host_pid": "9e6742732c60:1",
  "hash": "c377ae82d6b701b507cea1a789a0bca283020a36404a2c5611554c100db57c3f",
  "cid": "QmV1c377ae82d6b701b507cea1a789a0bca283020a36",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293750,
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
      "evaluated_at": 1760293750
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
  "sig": "8362ea1bc280534c240e46119017789694c144ab6f0ce6ffad0f2c0b2ff48400"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034128514
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 45461925, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760285763, 'matching_hash': '342851cb36b9daae'}}}