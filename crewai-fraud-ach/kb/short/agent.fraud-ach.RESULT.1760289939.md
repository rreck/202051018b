```json
{
  "id": "8a3e9b7e8e4cc10a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289939,
  "host_pid": "9e6742732c60:1",
  "hash": "091bb26c8b1a877ba2525d669057e4483fe23c0b1ff190b9b48e4809cfab20b9",
  "cid": "QmV1091bb26c8b1a877ba2525d669057e4483fe23c0b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289939,
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
      "evaluated_at": 1760289939
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
  "sig": "64241cea2ec83197f5a59940ec5a47a8b0c1b9b43da889f9026c39d1ef2f893a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270776467
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 137, 'threshold': 50, 'total_amount': 66978204, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 136, 'first_seen': 1760285763, 'matching_hash': 'a0c66d95a4fd4e21'}}}