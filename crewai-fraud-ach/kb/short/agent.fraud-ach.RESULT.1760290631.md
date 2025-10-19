```json
{
  "id": "2d87af6e9cac009d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290631,
  "host_pid": "9e6742732c60:1",
  "hash": "43cb6aea07ce48c4be8b543a18333b177ac86c62be117b9adc814008c316d7f5",
  "cid": "QmV143cb6aea07ce48c4be8b543a18333b177ac86c62",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290631,
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
      "evaluated_at": 1760290631
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
  "sig": "46fabd79232e2584e4fefed73e582324ad2fd7cbb023c0b9ee217dedeeb493e9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467134805
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 155, 'threshold': 50, 'total_amount': 42166975, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 154, 'first_seen': 1760285763, 'matching_hash': 'bc3c56d4b0e7489d'}}}