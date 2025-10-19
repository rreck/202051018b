```json
{
  "id": "40d1b2ef7c480c31",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287782,
  "host_pid": "9e6742732c60:1",
  "hash": "65634c4213b574e583e2574eae0d6b3b27c3dc128b2230e88f715e5037fbe219",
  "cid": "QmV165634c4213b574e583e2574eae0d6b3b27c3dc12",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287782,
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
      "evaluated_at": 1760287782
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
  "sig": "c3d51f8ba22bff1e53dcfc4bda1d20252e249f5f5f113bb9e86e74867db21d82"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000036487644
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 148, 'threshold': 50, 'total_amount': 62263156, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 147, 'first_seen': 1760284979, 'matching_hash': '0d42dcc750e3a553'}}}