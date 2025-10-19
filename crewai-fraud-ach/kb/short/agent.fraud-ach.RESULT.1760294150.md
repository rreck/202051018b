```json
{
  "id": "1a7eca592d279fbb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294150,
  "host_pid": "9e6742732c60:1",
  "hash": "428da01c491b9560a6a65af3ef2c9cc40729fb9c3517dfa2b8f4e0ee5dd13872",
  "cid": "QmV1428da01c491b9560a6a65af3ef2c9cc40729fb9c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294150,
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
      "evaluated_at": 1760294150
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_critical"
  ],
  "sig": "5cb497a37834bdfc7dd539f7d1830f5b42a6b70baa7232bdae5b41aa378ff067"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 111000025312922
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 1333948032, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285765, 'matching_hash': 'ec5c02804d9cd63b'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 5749776}}}