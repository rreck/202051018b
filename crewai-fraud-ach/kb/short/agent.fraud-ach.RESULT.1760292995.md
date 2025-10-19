```json
{
  "id": "fd4e00e4e7b69a37",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292995,
  "host_pid": "9e6742732c60:1",
  "hash": "14c560d17f97f361b9a2d5867c06eb410fa07ddcba06bbc8445784f0a24ccc91",
  "cid": "QmV114c560d17f97f361b9a2d5867c06eb410fa07ddc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292995,
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
      "evaluated_at": 1760292995
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
  "sig": "c6e5339fc1288087b770e99ea579f0dea68b8253f5aa69caa1aea665cf56818b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460191060
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 209, 'threshold': 50, 'total_amount': 72835664, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 208, 'first_seen': 1760285764, 'matching_hash': '1d882c6abf3447ef'}}}