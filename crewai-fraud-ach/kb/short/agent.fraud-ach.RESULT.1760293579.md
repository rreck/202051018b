```json
{
  "id": "4f88df78d9d843aa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293579,
  "host_pid": "9e6742732c60:1",
  "hash": "477026e03f96401994fccf6a6a9f0dd8719462695ce2386f38d6e7f1377fba15",
  "cid": "QmV1477026e03f96401994fccf6a6a9f0dd871946269",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293579,
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
      "evaluated_at": 1760293579
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
  "sig": "ce515b26ce11e9490f4e9f2490f6a369e3546ee945eeca2df248df20022d9e8c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274747147
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 17257006, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285763, 'matching_hash': '9bf7edfe04e96377'}}}