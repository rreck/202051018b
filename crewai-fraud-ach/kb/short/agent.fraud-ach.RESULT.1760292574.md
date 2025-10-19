```json
{
  "id": "4e160f8741e0ea7f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292574,
  "host_pid": "9e6742732c60:1",
  "hash": "9129c0efb87bcb852acee6cbb885a8f1b1231588843e33142a7273ec09188ec4",
  "cid": "QmV19129c0efb87bcb852acee6cbb885a8f1b1231588",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292574,
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
      "evaluated_at": 1760292574
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
  "sig": "6d99127fd2dd5c314c14ad91ea597d1f727177865f38e725ce70d582680c013f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028970082
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 200, 'threshold': 50, 'total_amount': 56735000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 199, 'first_seen': 1760285765, 'matching_hash': 'a98af89fc7548453'}}}