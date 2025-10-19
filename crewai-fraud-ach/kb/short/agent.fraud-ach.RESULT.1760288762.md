```json
{
  "id": "250280ee2c148a87",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288762,
  "host_pid": "9e6742732c60:1",
  "hash": "1e66de4542f3740265477a816e2832a1e53191a492ace890c420c6369337f4b2",
  "cid": "QmV11e66de4542f3740265477a816e2832a1e53191a4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288762,
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
      "evaluated_at": 1760288762
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
  "sig": "eaceb100501359d1ed8bb00f093f0dc63a1a8e510ac0c606659a10c565e03dd9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031029200
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 103, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 102, 'first_seen': 1760285763, 'matching_hash': '80e7fe619ff961e0'}}}