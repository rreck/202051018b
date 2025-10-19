```json
{
  "id": "af46888e95ab5e31",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293033,
  "host_pid": "9e6742732c60:1",
  "hash": "de59446cff8bcbe079a3e4dbdd6dad56673b287f67161a2890c8e7ae26f05e20",
  "cid": "QmV1de59446cff8bcbe079a3e4dbdd6dad56673b287f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293033,
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
      "evaluated_at": 1760293033
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
  "sig": "bd93686d63f4dd221637f0539077087a17ecb6f6868d318494f00893a85cf647"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591361030
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 210, 'threshold': 50, 'total_amount': 21583800, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 209, 'first_seen': 1760285763, 'matching_hash': '0549fb1f2e5dea5b'}}}