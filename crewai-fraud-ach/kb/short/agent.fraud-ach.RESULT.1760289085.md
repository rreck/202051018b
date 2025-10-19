```json
{
  "id": "6ccdc085680aeebb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289085,
  "host_pid": "9e6742732c60:1",
  "hash": "58a663326d29fb2d942bebcf2cdf37b7976ea53b620b347f35c9644df8c7b7c3",
  "cid": "QmV158a663326d29fb2d942bebcf2cdf37b7976ea53b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289085,
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
      "evaluated_at": 1760289085
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
  "sig": "57ff2d213bd6200bc8f959161d4ed77986d6316172c74720a05a3bda87ecb040"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034782199
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 113, 'threshold': 50, 'total_amount': 12289089, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 112, 'first_seen': 1760285763, 'matching_hash': '89ad1f50f76a063c'}}}