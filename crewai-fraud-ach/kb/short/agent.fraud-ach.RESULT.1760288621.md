```json
{
  "id": "17f82a209a1da018",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288621,
  "host_pid": "9e6742732c60:1",
  "hash": "4c7b6ca306136b157109fa9d9782d573024e2ee4d511e7642aed7bb18b92a03b",
  "cid": "QmV14c7b6ca306136b157109fa9d9782d573024e2ee4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288621,
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
      "evaluated_at": 1760288621
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
  "sig": "37b32dc1d2e5af8c2bf4a25adfa8c1e8cb5f2708101a4e29c58b6fa24c6cf98b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028116675
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 99, 'threshold': 50, 'total_amount': 33699105, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 98, 'first_seen': 1760285763, 'matching_hash': '276303153292771e'}}}