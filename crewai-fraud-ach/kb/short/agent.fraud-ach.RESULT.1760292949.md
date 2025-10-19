```json
{
  "id": "759e79898c05b160",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292949,
  "host_pid": "9e6742732c60:1",
  "hash": "3be2544ef78a7d3e28440149020a64f2c76fc14b1f05f482f841e4a1b2850155",
  "cid": "QmV13be2544ef78a7d3e28440149020a64f2c76fc14b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292949,
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
      "evaluated_at": 1760292949
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
  "sig": "0a94287695fd2272c382442a36673c5d8a2987bd81274080e722f6d132bc7e19"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596862432
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 208, 'threshold': 50, 'total_amount': 42443648, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 207, 'first_seen': 1760285764, 'matching_hash': 'ec6d2f2d96a1a77c'}}}