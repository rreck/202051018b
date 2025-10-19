```json
{
  "id": "e8cb79ed00378cbb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292543,
  "host_pid": "9e6742732c60:1",
  "hash": "6f9dc72f91d5a44e270ce371efdcae5a56afb75cda8d0d1f645ddf5b97715acb",
  "cid": "QmV16f9dc72f91d5a44e270ce371efdcae5a56afb75c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292543,
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
      "evaluated_at": 1760292543
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
  "sig": "6a73a337b66bb0cfca30fd6718c97edef809f528bb362218b6d17cba2e4b842c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025654087
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 200, 'threshold': 50, 'total_amount': 27959000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 199, 'first_seen': 1760285763, 'matching_hash': '431eabbdd05dc2b1'}}}maly': {'fraud_detected': True, 'risk_score': 87, 'details': {'zscore': 4.79, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9144651}}}