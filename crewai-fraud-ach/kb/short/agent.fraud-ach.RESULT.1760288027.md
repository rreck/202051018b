```json
{
  "id": "49e7a869098d3d7a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288027,
  "host_pid": "9e6742732c60:1",
  "hash": "1022cc59658c0859615b7c990e871c31eee653a88245b609571015ccab795604",
  "cid": "QmV11022cc59658c0859615b7c990e871c31eee653a8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288027,
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
      "evaluated_at": 1760288027
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
  "sig": "db2733a1654eab2a3e0e9fb80d77b826cb7e29fb6189e7f380e87ea63a081a49"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037423947
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 80, 'threshold': 50, 'total_amount': 15976080, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 79, 'first_seen': 1760285763, 'matching_hash': '5528b0ca47a44e30'}}}