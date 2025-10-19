```json
{
  "id": "b1d3dba2bcda7b05",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292142,
  "host_pid": "9e6742732c60:1",
  "hash": "76c3bb66cd43e325ebcceb60e0c4b8307f9dd5ec9eef791c241c09cdec854072",
  "cid": "QmV176c3bb66cd43e325ebcceb60e0c4b8307f9dd5ec",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292142,
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
      "evaluated_at": 1760292142
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
  "sig": "f867452a09323eb67dae3a56e3cab787b8504f71346b2194a193ae9e0477b91b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469615703
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 191, 'threshold': 50, 'total_amount': 36386837, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 190, 'first_seen': 1760285763, 'matching_hash': '33adc30ff3203421'}}}