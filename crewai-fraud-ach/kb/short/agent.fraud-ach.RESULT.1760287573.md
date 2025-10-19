```json
{
  "id": "b4eb1ae570bd7851",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287573,
  "host_pid": "9e6742732c60:1",
  "hash": "42e9fb38be65b7e8d2ebdc112daae370dd33bcac9fe8728016e7286224884e61",
  "cid": "QmV142e9fb38be65b7e8d2ebdc112daae370dd33bcac",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287573,
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
      "evaluated_at": 1760287573
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
  "sig": "68f7681c8e8ec21e8f3a8108d888648ed6e6c8bd0aa70021340418978b5bc2f8"
}
```

Fraud detected: duplicate_transaction (score: 82)
Transaction: 111000023881991
Details: {'velocity': {'fraud_detected': True, 'risk_score': 80, 'details': {'transaction_count': 65, 'threshold': 50, 'total_amount': 15424305, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 64, 'first_seen': 1760285763, 'matching_hash': 'ea388fdaad903558'}}}