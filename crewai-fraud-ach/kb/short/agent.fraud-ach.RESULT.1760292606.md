```json
{
  "id": "0f26155358c7bd94",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292606,
  "host_pid": "9e6742732c60:1",
  "hash": "149ac32c73d516e6ecac28b35556fc5445aba9bfb2dc61be1e714d53d96a5431",
  "cid": "QmV1149ac32c73d516e6ecac28b35556fc5445aba9bf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292606,
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
      "evaluated_at": 1760292606
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
  "sig": "bd4879762c32ee690d8321e565696a0d03d890837b3337b88e3504847118f339"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154224764
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 201, 'threshold': 50, 'total_amount': 48538485, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 200, 'first_seen': 1760285763, 'matching_hash': '73218c90107a537b'}}}maly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 5595688}}}