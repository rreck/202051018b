```json
{
  "id": "581d122b99beaa4f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290758,
  "host_pid": "9e6742732c60:1",
  "hash": "0571be5cf397b02063c52fc34c8cbba09471c022385421eb5ad36f2ff918efb7",
  "cid": "QmV10571be5cf397b02063c52fc34c8cbba09471c022",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290758,
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
      "evaluated_at": 1760290758
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
  "sig": "d3696a3c612bb0cfe22d58bcf0031f0c3fe87feaf25b5d21caae43c46b548a31"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469832017
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 158, 'threshold': 50, 'total_amount': 49383058, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 157, 'first_seen': 1760285765, 'matching_hash': '99e095073411ccc4'}}}