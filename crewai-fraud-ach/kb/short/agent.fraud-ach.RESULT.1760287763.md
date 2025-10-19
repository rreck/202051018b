```json
{
  "id": "fd0f355e8896a694",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287763,
  "host_pid": "9e6742732c60:1",
  "hash": "e0c005e3f4cbf7e6072e34a6f42c31bf06581daf8a39bac19d329140a9b4d39d",
  "cid": "QmV1e0c005e3f4cbf7e6072e34a6f42c31bf06581daf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287763,
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
      "evaluated_at": 1760287763
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
  "sig": "40d30d29deab448a2239ae74276c65b3c6c3cd61c98ac0887505182816ec610e"
}
```

Fraud detected: duplicate_transaction (score: 88)
Transaction: 021000025375881
Details: {'velocity': {'fraud_detected': True, 'risk_score': 92, 'details': {'transaction_count': 71, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 70, 'first_seen': 1760285765, 'matching_hash': '7f563b0766db4821'}}}