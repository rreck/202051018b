```json
{
  "id": "4ad83f7574290fd8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294297,
  "host_pid": "9e6742732c60:1",
  "hash": "856983d357a7f5fa9e89b8cb493bd6704fe34ad0708409caeea0cf237deffeac",
  "cid": "QmV1856983d357a7f5fa9e89b8cb493bd6704fe34ad0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294297,
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
      "evaluated_at": 1760294297
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
  "sig": "60f1a337a1e18bd522274144be67fe86baace06c2c45f3592b370e00fb88e88e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241250323
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 235, 'threshold': 50, 'total_amount': 23263355, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 234, 'first_seen': 1760285763, 'matching_hash': 'd18939bbbb7c2a14'}}}