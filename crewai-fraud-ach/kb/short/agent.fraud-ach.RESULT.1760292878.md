```json
{
  "id": "3485b6da67131419",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292878,
  "host_pid": "9e6742732c60:1",
  "hash": "c46116315b4eeefd952a59fd96d7d0ea5e7cb2a2af2b8fa1263548ab0bc89907",
  "cid": "QmV1c46116315b4eeefd952a59fd96d7d0ea5e7cb2a2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292878,
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
      "evaluated_at": 1760292878
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
  "sig": "14440ed2f2dec42e7e68965c65f632109d6c9768b10c81ee1429eed5f84472c0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000020120978
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 207, 'threshold': 50, 'total_amount': 19955214, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 206, 'first_seen': 1760285763, 'matching_hash': '55bccccaf90262bb'}}}unt_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}