```json
{
  "id": "c46149e5e5bea16f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292297,
  "host_pid": "9e6742732c60:1",
  "hash": "755bc14c865427b269c1201e678786a825d7f2cecc977c93f41f24cd1c9824a2",
  "cid": "QmV1755bc14c865427b269c1201e678786a825d7f2ce",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292297,
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
      "evaluated_at": 1760292297
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
  "sig": "7487d8f52e0b649750101ecca6d8e728e09a439af5082c81c5177067186bb3df"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242521033
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 194, 'threshold': 50, 'total_amount': 12906626, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 193, 'first_seen': 1760285765, 'matching_hash': 'cfb80109aa92585a'}}}