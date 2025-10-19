```json
{
  "id": "b834ec2fff8daae1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287805,
  "host_pid": "9e6742732c60:1",
  "hash": "7b166f764734761950c4fba051cad48a7deeee86da78c830f4b0105b389c59cd",
  "cid": "QmV17b166f764734761950c4fba051cad48a7deeee86",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287805,
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
      "evaluated_at": 1760287805
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
  "sig": "b6760dfb28b23c015a2acc5c73b76a4ed1bcb9babe961792c7dbed9108fe59fd"
}
```

Fraud detected: duplicate_transaction (score: 90)
Transaction: 063100274159227
Details: {'velocity': {'fraud_detected': True, 'risk_score': 96, 'details': {'transaction_count': 73, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 72, 'first_seen': 1760285763, 'matching_hash': 'c6403d45da933f2b'}}}