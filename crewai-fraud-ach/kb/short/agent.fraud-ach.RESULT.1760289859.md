```json
{
  "id": "659524e441268017",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289859,
  "host_pid": "9e6742732c60:1",
  "hash": "5374913ef52bffb375a52b258d7ea351c1d27c557bf9cb7acd21ddf27fbadc2d",
  "cid": "QmV15374913ef52bffb375a52b258d7ea351c1d27c55",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289859,
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
      "evaluated_at": 1760289859
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
  "sig": "808d0a8a966cd99ad173193ca9a31d90846d3394cbd65484192610e0a1b9f898"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278619879
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 135, 'threshold': 50, 'total_amount': 45725445, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 134, 'first_seen': 1760285763, 'matching_hash': 'bfc334a18daf8fbf'}}}