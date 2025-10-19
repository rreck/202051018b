```json
{
  "id": "c028c369d74f915b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287522,
  "host_pid": "9e6742732c60:1",
  "hash": "7cba0671b68994d98557c4f745420f673309e10206cf4da297514aebc183f7f0",
  "cid": "QmV17cba0671b68994d98557c4f745420f673309e102",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287522,
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
      "evaluated_at": 1760287522
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
  "sig": "b4f5d69e63eef5902751501db8b6d9b353ac78bec04340e6e4bcb976bc18232a"
}
```

Fraud detected: duplicate_transaction (score: 80)
Transaction: 111000024460145
Details: {'velocity': {'fraud_detected': True, 'risk_score': 76, 'details': {'transaction_count': 63, 'threshold': 50, 'total_amount': 15977241, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 62, 'first_seen': 1760285763, 'matching_hash': '6128e7e8f1f7694a'}}}}}}'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6481360}}}