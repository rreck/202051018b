```json
{
  "id": "6d925e183643dfeb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291494,
  "host_pid": "9e6742732c60:1",
  "hash": "55ef32c0e5bc418287da80a6ddd8b830dae2f78242d52a058384791ac431f30a",
  "cid": "QmV155ef32c0e5bc418287da80a6ddd8b830dae2f782",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291494,
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
      "evaluated_at": 1760291494
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
  "sig": "a96f521756ca27dbcd99ba80ea725530bc6c9b798a1248fe0cce1394beb9b114"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249127775
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 176, 'threshold': 50, 'total_amount': 25316544, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 175, 'first_seen': 1760285763, 'matching_hash': '35c1bd481e0f1f5f'}}}