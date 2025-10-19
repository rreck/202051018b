```json
{
  "id": "bb9b0badc01460cc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290368,
  "host_pid": "9e6742732c60:1",
  "hash": "0efba7e3c1def77c195356162ce2bb9481e115323243d0c5c29770d525cbe48a",
  "cid": "QmV10efba7e3c1def77c195356162ce2bb9481e11532",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290368,
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
      "evaluated_at": 1760290368
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
  "sig": "db54269ebe9afa1e6458c52b52926f4ba18cb1924d0ab39710e654a5a29458fe"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025001530
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 148, 'threshold': 50, 'total_amount': 35735192, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 147, 'first_seen': 1760285765, 'matching_hash': 'c7ad70870577ca51'}}}