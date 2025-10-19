```json
{
  "id": "03c0ffbfbd4811e6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288360,
  "host_pid": "9e6742732c60:1",
  "hash": "1d6508c928f986578f37685f83f30763b2289e554cb23ac8025f5770dcf40fb6",
  "cid": "QmV11d6508c928f986578f37685f83f30763b2289e55",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288360,
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
      "evaluated_at": 1760288360
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
  "sig": "d0a9e0ef22a7afbe0e85c847598553a2215401557a6361e24b59a07705e827cc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026044300
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 91, 'threshold': 50, 'total_amount': 34972483, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 90, 'first_seen': 1760285763, 'matching_hash': '19d391c08a2c00ab'}}}