```json
{
  "id": "02c4344e2cfd0dee",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288833,
  "host_pid": "9e6742732c60:1",
  "hash": "bec3f69267a3f154eea6ec0a0cd22d94ec210f3a473bb37fb8483f8d814e2ed5",
  "cid": "QmV1bec3f69267a3f154eea6ec0a0cd22d94ec210f3a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288833,
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
      "evaluated_at": 1760288833
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
  "sig": "09a990182d158249a1f6641089892d26e7072117d2c3a542a276f7d87fc9e7ce"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465368597
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 105, 'threshold': 50, 'total_amount': 26117490, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 104, 'first_seen': 1760285765, 'matching_hash': 'f57f84d557436d23'}}}