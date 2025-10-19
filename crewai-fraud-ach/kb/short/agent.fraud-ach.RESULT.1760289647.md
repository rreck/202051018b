```json
{
  "id": "177abf68f0b2abed",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289647,
  "host_pid": "9e6742732c60:1",
  "hash": "fde94b03c19905499728ccdb8ad8dde1e966ce2bf6dbab74204d2d0e0571df9e",
  "cid": "QmV1fde94b03c19905499728ccdb8ad8dde1e966ce2b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289647,
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
      "evaluated_at": 1760289647
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
  "sig": "daf8ac3f7d06b26b9cfedffe4a20c08aaff6744677056e202ba428a46a5f71dd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032958974
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 129, 'threshold': 50, 'total_amount': 54302550, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 128, 'first_seen': 1760285763, 'matching_hash': '718043100f50114f'}}}