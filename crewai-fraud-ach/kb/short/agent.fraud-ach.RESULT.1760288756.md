```json
{
  "id": "c23eee73dd213abe",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288756,
  "host_pid": "9e6742732c60:1",
  "hash": "dba5691f40c770fe27b411b8abb9c38d50cba10c88c25d09322d892dddb6ed71",
  "cid": "QmV1dba5691f40c770fe27b411b8abb9c38d50cba10c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288756,
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
      "evaluated_at": 1760288756
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
  "sig": "69d24ef6e215e2c8e2f0f9a04ecd20de4c4858e6fa6c82a451ad4a33c133db73"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592426992
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 103, 'threshold': 50, 'total_amount': 43958031, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 102, 'first_seen': 1760285763, 'matching_hash': '6c96fa15a49bffda'}}}