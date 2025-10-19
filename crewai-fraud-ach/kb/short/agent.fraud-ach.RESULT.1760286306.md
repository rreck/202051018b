```json
{
  "id": "d67213c4d2805fff",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286306,
  "host_pid": "9e6742732c60:1",
  "hash": "91392d84f985799ee3fba8e9a4ba5b7c7aaed978efd1fa7cf13fb4b285c2cb0a",
  "cid": "QmV191392d84f985799ee3fba8e9a4ba5b7c7aaed978",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286306,
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
      "evaluated_at": 1760286306
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
  "sig": "fe20fc21f5b701debe378ef934ee6f936f712705b0ce20e9a985087f2ddcc793"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030256978
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 97, 'threshold': 50, 'total_amount': 36816738, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 96, 'first_seen': 1760284979, 'matching_hash': 'a2caca18f22a9a3d'}}}, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6481360}}}