```json
{
  "id": "62db3609fe468962",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289692,
  "host_pid": "9e6742732c60:1",
  "hash": "13526240ab14027125f46fa8c9429f5f8dcae680bba68318af1d0dff028164e0",
  "cid": "QmV113526240ab14027125f46fa8c9429f5f8dcae680",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289692,
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
      "evaluated_at": 1760289692
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
  "sig": "e3bcff0dd6bbe4ffbd51e0ae406c6487ebf04b9718b2b1dbc35859908a17e191"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596862432
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 130, 'threshold': 50, 'total_amount': 26527280, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 129, 'first_seen': 1760285764, 'matching_hash': 'ec6d2f2d96a1a77c'}}}