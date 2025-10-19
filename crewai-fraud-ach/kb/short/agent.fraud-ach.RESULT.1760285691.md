```json
{
  "id": "0014339de53a29bc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285691,
  "host_pid": "9e6742732c60:1",
  "hash": "4c1abd54aec945898def4b95cfcdbd8ba1380ab4c59e51edf91c22b45358ebce",
  "cid": "QmV14c1abd54aec945898def4b95cfcdbd8ba1380ab4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285691,
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
      "evaluated_at": 1760285691
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
  "sig": "c54508c6224cf36f9b3293c7f558171b2b39e940317193360a3c174fedc8fdfc"
}
```

Fraud detected: duplicate_transaction (score: 87)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 90, 'details': {'transaction_count': 70, 'threshold': 50, 'total_amount': 29497580, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 69, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}