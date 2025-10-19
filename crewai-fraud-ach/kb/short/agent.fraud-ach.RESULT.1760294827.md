```json
{
  "id": "435121e5d17c8f40",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294827,
  "host_pid": "9e6742732c60:1",
  "hash": "3063e90d9c8796388c3f22cd217a4351c5db550a6342787a1fc19d9d0f6a5d7b",
  "cid": "QmV13063e90d9c8796388c3f22cd217a4351c5db550a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294827,
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
      "evaluated_at": 1760294827
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
  "sig": "f4b1aaf4a8cacc9b9d3f919bdb25eaab3ea258d71ebbb657ebadc06226e7cc3e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272098114
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 101540495, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285764, 'matching_hash': '010bb0d7cfc5cc6e'}}}