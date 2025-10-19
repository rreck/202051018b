```json
{
  "id": "1cb142046378c484",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288116,
  "host_pid": "9e6742732c60:1",
  "hash": "636a90c709bb9d4bd6aaca2fd76f8dc135e42adf38e2d2c946700ff795ffd934",
  "cid": "QmV1636a90c709bb9d4bd6aaca2fd76f8dc135e42adf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288116,
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
      "evaluated_at": 1760288116
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
  "sig": "630c0da33aaffe5d27d7382438e9363fc8cad9e2bed72e0b3fc2bdb4c869eb73"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152345106
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 83, 'threshold': 50, 'total_amount': 38504032, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 82, 'first_seen': 1760285764, 'matching_hash': '244a38e8c31df032'}}}}}