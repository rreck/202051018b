```json
{
  "id": "ca167c4b8f9c9beb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293510,
  "host_pid": "9e6742732c60:1",
  "hash": "ca141f9009f59da44f73edc9f6a0ea7d8d65c2e689ebf4ffb8e99fc014f107fa",
  "cid": "QmV1ca141f9009f59da44f73edc9f6a0ea7d8d65c2e6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293510,
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
      "evaluated_at": 1760293510
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
  "sig": "53556b0a73fa241df2ecf26f93b7ceb3cd9a33b41d9a4a1a642b70ac42f586f3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158076407
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 220, 'threshold': 50, 'total_amount': 32679900, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 219, 'first_seen': 1760285763, 'matching_hash': 'bd01239b3993ff64'}}}