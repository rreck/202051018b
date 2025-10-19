```json
{
  "id": "3b185bdf2168cf7a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292465,
  "host_pid": "9e6742732c60:1",
  "hash": "f7a1fad60ae058992c269300d80205aa39af4364eb777b1d37bfa588a790bc41",
  "cid": "QmV1f7a1fad60ae058992c269300d80205aa39af4364",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292465,
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
      "evaluated_at": 1760292465
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
  "sig": "b54590227751e7e5f4efebecfe39e2113e4af1ef0c24212d915d57aee0a5c7ca"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243890645
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 198, 'threshold': 50, 'total_amount': 36054810, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 197, 'first_seen': 1760285764, 'matching_hash': '25ed426365fec5d8'}}}