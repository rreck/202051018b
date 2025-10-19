```json
{
  "id": "ff106e3df60ce681",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290950,
  "host_pid": "9e6742732c60:1",
  "hash": "2f0847bc97243a950fb6adaade6aff16736ca8239e005df0fd4c8214c2504a09",
  "cid": "QmV12f0847bc97243a950fb6adaade6aff16736ca823",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290950,
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
      "evaluated_at": 1760290950
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
  "sig": "d05ab9d1c34e97feaa555fc682444fed9709fa6d3fe4225d951cc971d5095a8c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028860438
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 163, 'threshold': 50, 'total_amount': 47841804, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 162, 'first_seen': 1760285763, 'matching_hash': '1ce58b471eab5597'}}}aly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 5062727}}}