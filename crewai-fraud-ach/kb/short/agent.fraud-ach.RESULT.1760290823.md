```json
{
  "id": "98423e7f2a4baf57",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290823,
  "host_pid": "9e6742732c60:1",
  "hash": "fa6f88b8399d34dde19f82ed98f20a520f7b3400e4252e302c08859c5fb003d4",
  "cid": "QmV1fa6f88b8399d34dde19f82ed98f20a520f7b3400",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290823,
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
      "evaluated_at": 1760290823
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
  "sig": "09348226264e1d8e2b89565e8a1eed40d24499be41368d532c1b08e9d2b9d85f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465280061
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 160, 'threshold': 50, 'total_amount': 21279680, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 159, 'first_seen': 1760285763, 'matching_hash': '24e243e35a5cb5f6'}}}