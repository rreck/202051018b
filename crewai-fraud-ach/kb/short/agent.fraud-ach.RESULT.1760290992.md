```json
{
  "id": "6003825e160cc87d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290992,
  "host_pid": "9e6742732c60:1",
  "hash": "75a24496a7bb3f6c99d33a6c8df7b254f3fbd272425c1438727b924b17d01b3c",
  "cid": "QmV175a24496a7bb3f6c99d33a6c8df7b254f3fbd272",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290992,
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
      "evaluated_at": 1760290992
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
  "sig": "bbf35a4729e0a6ae8935293575fe16d213c3481e7b5b97eddeaadb70043574ef"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244797937
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 164, 'threshold': 50, 'total_amount': 64941048, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 163, 'first_seen': 1760285765, 'matching_hash': 'e00995c9aab9b89d'}}}