```json
{
  "id": "d60d36a147843aae",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294086,
  "host_pid": "9e6742732c60:1",
  "hash": "21a7aa228a0528126205d22c5e2c08c704bee97788e0a54d85c1f08bbec3e326",
  "cid": "QmV121a7aa228a0528126205d22c5e2c08c704bee977",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294086,
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
      "evaluated_at": 1760294086
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
  "sig": "4f5da5107cc94455254832da483e53a45e99bd36dca1c6e1cda9bb9e1dbc3dfd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598076965
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 36223572, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285763, 'matching_hash': '05e01649c2d43b8b'}}}