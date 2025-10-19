```json
{
  "id": "ec44e8eef893e890",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291309,
  "host_pid": "9e6742732c60:1",
  "hash": "2600c62cb3d55ecbb2872e70a4ff9bbc8c6384f88e170e70acd989c5558124ed",
  "cid": "QmV12600c62cb3d55ecbb2872e70a4ff9bbc8c6384f8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291309,
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
      "evaluated_at": 1760291309
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
  "sig": "d845cfbd51666f48ef09b91dac9541202a97ef3061de778b162e2e1a88a248cf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593787585
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 172, 'threshold': 50, 'total_amount': 74648860, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 171, 'first_seen': 1760285763, 'matching_hash': '27c7bfe810f6d733'}}}