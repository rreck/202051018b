```json
{
  "id": "994ebe5261bb7242",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288365,
  "host_pid": "9e6742732c60:1",
  "hash": "3ddf4f90a62e5e8e18fae87614e52f7867b1562e0a65d340c1c2035d17586639",
  "cid": "QmV13ddf4f90a62e5e8e18fae87614e52f7867b1562e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288365,
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
      "evaluated_at": 1760288365
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
  "sig": "656692528abd8b5e1c59745df49af4d58c54dd885ea737c6840575ccf528a5b8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153734827
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 91, 'threshold': 50, 'total_amount': 44903495, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 90, 'first_seen': 1760285764, 'matching_hash': 'f575a9f929aab221'}}}