```json
{
  "id": "565003a7641de0ed",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291537,
  "host_pid": "9e6742732c60:1",
  "hash": "50235388b7ab2d1341f71036eed872f054bcf4eb3210d3d585db6a20edbe71e2",
  "cid": "QmV150235388b7ab2d1341f71036eed872f054bcf4eb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291537,
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
      "evaluated_at": 1760291537
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
  "sig": "35907cdc7346a5252d598cd42dc1cffed12cfcf09c4f9e38fd09614250f0be6e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597735648
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 177, 'threshold': 50, 'total_amount': 44577981, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 176, 'first_seen': 1760285763, 'matching_hash': '529f1dc61ac58982'}}}