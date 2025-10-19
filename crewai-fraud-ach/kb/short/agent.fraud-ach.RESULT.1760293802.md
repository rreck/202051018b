```json
{
  "id": "b5e6bec977a46898",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293802,
  "host_pid": "9e6742732c60:1",
  "hash": "3c225f07035b514476fd990ea4da4fa0a464605cb16b4f29e9b2e2a3b793ac40",
  "cid": "QmV13c225f07035b514476fd990ea4da4fa0a464605c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293802,
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
      "evaluated_at": 1760293802
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
  "sig": "14529cddb6101efa24eacd7da7877dd9b6c943b4e9e5d609a98597c56435df93"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592077072
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 52858914, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285763, 'matching_hash': '86add4fc1587ca1b'}}}