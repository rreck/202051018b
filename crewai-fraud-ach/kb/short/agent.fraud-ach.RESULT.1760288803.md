```json
{
  "id": "25c48bba4f705078",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288803,
  "host_pid": "9e6742732c60:1",
  "hash": "2461773867f8d960ab31cd7ed4c6ee34e255809ce7e865c1a5b5b4cae67fd97a",
  "cid": "QmV12461773867f8d960ab31cd7ed4c6ee34e255809c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288803,
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
      "evaluated_at": 1760288803
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
  "sig": "932c98d9806b9f1a2d2b9b8e87aaf8a3b60d68789326cc95cad8ec3693019e37"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027607406
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 104, 'threshold': 50, 'total_amount': 11522264, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 103, 'first_seen': 1760285765, 'matching_hash': '504131d6dff02852'}}}