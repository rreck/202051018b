```json
{
  "id": "ea3abfc9e30433f7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290274,
  "host_pid": "9e6742732c60:1",
  "hash": "dda20737ab4a7d52ea1a2c353a0b52e37eaa3e86a3fe98bffebc4a893f8edf3a",
  "cid": "QmV1dda20737ab4a7d52ea1a2c353a0b52e37eaa3e86",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290274,
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
      "evaluated_at": 1760290274
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
  "sig": "4f791e12e750c9b50e3844d5ecf6003dd388e809a949683687e30ef9d68d404a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274546383
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 146, 'threshold': 50, 'total_amount': 38628680, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 145, 'first_seen': 1760285763, 'matching_hash': '76da04c5629ac502'}}}