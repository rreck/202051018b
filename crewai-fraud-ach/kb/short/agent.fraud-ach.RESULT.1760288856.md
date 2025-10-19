```json
{
  "id": "71bb0924d93afdb7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288856,
  "host_pid": "9e6742732c60:1",
  "hash": "c6e288bb46c1b28a666a7ad3b15b33aaf6ffde77712893454695379b3b3ba19e",
  "cid": "QmV1c6e288bb46c1b28a666a7ad3b15b33aaf6ffde77",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288856,
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
      "evaluated_at": 1760288856
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
  "sig": "3a2b8df4cf2d121ba28df6ffdab78c05e75c3013f89ed2ee0e6534964fc84e89"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240708140
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 106, 'threshold': 50, 'total_amount': 11312002, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 105, 'first_seen': 1760285763, 'matching_hash': 'e22b1a9baac54cae'}}}