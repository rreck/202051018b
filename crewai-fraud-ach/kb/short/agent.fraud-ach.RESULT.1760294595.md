```json
{
  "id": "cf9689ac8c393d5d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294595,
  "host_pid": "9e6742732c60:1",
  "hash": "3a3b5c2db1b952fdc95b925a5ece6f616edc324956acddd0d0315ab3266da18f",
  "cid": "QmV13a3b5c2db1b952fdc95b925a5ece6f616edc3249",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294595,
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
      "evaluated_at": 1760294595
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
  "sig": "6e26b7a85322b2d6b7cfe0b7660c7c4c6358ce98d2234315d5ae3725e675a959"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028841300
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 45051335, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285763, 'matching_hash': 'f5bed59f6c250fae'}}}