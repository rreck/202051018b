```json
{
  "id": "a3a7b55e82d87449",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291396,
  "host_pid": "9e6742732c60:1",
  "hash": "b7c5ec3220008e29303c1b4be7a07792f2dcec0061f88be4a58bd1ecfdb2d2e6",
  "cid": "QmV1b7c5ec3220008e29303c1b4be7a07792f2dcec00",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291396,
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
      "evaluated_at": 1760291396
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
  "sig": "8118d215d53eb48dca4289a05e0ab5c32e811159444486ebe957dc890bf931b2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025319716
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 174, 'threshold': 50, 'total_amount': 44493714, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 173, 'first_seen': 1760285764, 'matching_hash': '46cae66c8ff70b91'}}}maly': {'fraud_detected': True, 'risk_score': 73, 'details': {'zscore': 3.38, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6665760}}}