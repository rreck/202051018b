```json
{
  "id": "1499dad913ab6001",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287081,
  "host_pid": "9e6742732c60:1",
  "hash": "f7ed2be678a50a0661183a891f290685a838d133e74f52903a4ee74131f425ed",
  "cid": "QmV1f7ed2be678a50a0661183a891f290685a838d133",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287081,
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
      "evaluated_at": 1760287081
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "545f27151f0e79b3a22d4bee1dde75e5666f72405bc81befcea0d528e5de6653"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 021000020143117
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11750000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 46, 'first_seen': 1760285765, 'matching_hash': '83c798d1c8d9cfec'}}}