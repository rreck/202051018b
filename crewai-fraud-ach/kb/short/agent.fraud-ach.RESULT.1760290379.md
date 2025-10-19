```json
{
  "id": "73f26a065b892462",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290379,
  "host_pid": "9e6742732c60:1",
  "hash": "ef0a9e1587e25c7622859946ef8803d70666d5a5e4208ec6a537622fb447211d",
  "cid": "QmV1ef0a9e1587e25c7622859946ef8803d70666d5a5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290379,
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
      "evaluated_at": 1760290379
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
  "sig": "ef8f72bc8a600ba972283f97ee330afcc1a818e4ad2c3f6deb015a230222ffab"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000035593386
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 149, 'threshold': 50, 'total_amount': 17783895, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 148, 'first_seen': 1760285763, 'matching_hash': '6253d15ae41563d2'}}}