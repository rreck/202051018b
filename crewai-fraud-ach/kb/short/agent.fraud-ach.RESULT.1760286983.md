```json
{
  "id": "7ad8d8e9edffefd2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286983,
  "host_pid": "9e6742732c60:1",
  "hash": "8ccafb8a3893fcc0d2edb9816b6638dc2705b8d238437e1e78dfa4f9fad52688",
  "cid": "QmV18ccafb8a3893fcc0d2edb9816b6638dc2705b8d2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286983,
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
      "evaluated_at": 1760286983
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
  "sig": "03f45254cd9941329fa862ad8418f758837e8f2c7bb069cc2af7c96f33720703"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000034056272
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 43, 'first_seen': 1760285763, 'matching_hash': 'aae4e2a94575911d'}}}ue, 'risk_score': 85, 'details': {'duplicate_count': 43, 'first_seen': 1760285763, 'matching_hash': 'aef06f437446325c'}}}