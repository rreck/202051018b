```json
{
  "id": "0a9ce4a1730e23c6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293240,
  "host_pid": "9e6742732c60:1",
  "hash": "36b80ca3d0fe17fd591ec756d30a3beb781b6f41ff6143d5c36caf7ed7dae9e7",
  "cid": "QmV136b80ca3d0fe17fd591ec756d30a3beb781b6f41",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293240,
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
      "evaluated_at": 1760293240
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
  "sig": "21165a9c06599aae4022c38c02628cc6f6d1baf2dd8f90e5faa232937a6c74cf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039663431
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 214, 'threshold': 50, 'total_amount': 31869522, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 213, 'first_seen': 1760285764, 'matching_hash': '33f644fe289ea89d'}}}