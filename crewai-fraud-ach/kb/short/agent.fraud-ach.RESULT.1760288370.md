```json
{
  "id": "2c2b7cb8a4c36298",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288370,
  "host_pid": "9e6742732c60:1",
  "hash": "62f50162cba368ba73f85036d209e00a0e509887a17348ccd456d6269fc14f76",
  "cid": "QmV162f50162cba368ba73f85036d209e00a0e509887",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288370,
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
      "evaluated_at": 1760288370
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
  "sig": "7b95853729a96f3a25a1b565b602c182da951598961d8e685496d216c5b07d36"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154990255
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 91, 'threshold': 50, 'total_amount': 11284546, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 90, 'first_seen': 1760285763, 'matching_hash': '800f0de895a214ba'}}}