```json
{
  "id": "7da9255527e6b731",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290854,
  "host_pid": "9e6742732c60:1",
  "hash": "e9b637550fe386a91b3250f183f06b225e776c7ec20546cdd5c0f6c9d6914fc1",
  "cid": "QmV1e9b637550fe386a91b3250f183f06b225e776c7e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290854,
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
      "evaluated_at": 1760290854
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
  "sig": "c7dbc29a69dc6927e76030d2eaaa8e7d4c9c1956a700ac4902c41eb7852b9457"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274851410
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 161, 'threshold': 50, 'total_amount': 19928258, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 160, 'first_seen': 1760285763, 'matching_hash': '05e1730ec720465d'}}}unt_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}