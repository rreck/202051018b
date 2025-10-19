```json
{
  "id": "aced15c6009c7ddd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291147,
  "host_pid": "9e6742732c60:1",
  "hash": "bf8b49592ee3fb37770e718b237b4e2d8507bcf0fe526bba5ed6ba83b489d2fc",
  "cid": "QmV1bf8b49592ee3fb37770e718b237b4e2d8507bcf0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291147,
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
      "evaluated_at": 1760291147
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
  "sig": "2dd43a1b0b5cdf7f93d3a3e18172dfebb54d063694f69a4319bb3510cd10aad9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022233458
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 168, 'threshold': 50, 'total_amount': 47511072, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 167, 'first_seen': 1760285763, 'matching_hash': '02c54d650b9e4b50'}}}