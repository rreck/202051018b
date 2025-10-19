```json
{
  "id": "d405e7fe69a393f4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287894,
  "host_pid": "9e6742732c60:1",
  "hash": "ae7c186aa070ba184f89fcf9521d3b6ff597cc5e00b79ae9fdef2ee8f28c0e0d",
  "cid": "QmV1ae7c186aa070ba184f89fcf9521d3b6ff597cc5e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287894,
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
      "evaluated_at": 1760287894
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
  "sig": "970947e4365b17b563a182d1a6f3b9a0f1ce37c3f41adaca8953897c3b05539d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038073979
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 76, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 75, 'first_seen': 1760285763, 'matching_hash': '05e8b4bb68b88ac5'}}}een': 1760285763, 'matching_hash': 'b939c4c4097f2f1f'}}}