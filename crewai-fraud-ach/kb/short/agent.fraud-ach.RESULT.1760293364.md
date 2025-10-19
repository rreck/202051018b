```json
{
  "id": "4d257010773e68c4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293364,
  "host_pid": "9e6742732c60:1",
  "hash": "1f61b22a41efc7fd85866439b420ae2cb49a3ae20064aa84fefc536d0af1809a",
  "cid": "QmV11f61b22a41efc7fd85866439b420ae2cb49a3ae2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293364,
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
      "evaluated_at": 1760293364
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
  "sig": "5e6a28e5e4256710557f9a74c00f15f203d2d9398979e6b2d1251b61b4f6537c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249232395
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 217, 'threshold': 50, 'total_amount': 79212812, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 216, 'first_seen': 1760285764, 'matching_hash': '83f71011b8a0f970'}}}