```json
{
  "id": "c25c81fa946d2299",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291625,
  "host_pid": "9e6742732c60:1",
  "hash": "af36fa4962a93607c3304a358e584fb8d1ea6f7baed914e4f2eebfdd60d1e85d",
  "cid": "QmV1af36fa4962a93607c3304a358e584fb8d1ea6f7b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291625,
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
      "evaluated_at": 1760291625
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
  "sig": "0b6d969b0289f93563dcd831f35a95302d65fdb214344f6a20b39aa85be60145"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593702879
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 179, 'threshold': 50, 'total_amount': 35334779, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 178, 'first_seen': 1760285763, 'matching_hash': '1b01d510f5fcfc0c'}}}