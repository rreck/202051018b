```json
{
  "id": "eabd2dfce6c10f95",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292599,
  "host_pid": "9e6742732c60:1",
  "hash": "4d7ce56635a39f648257465a68dc04074a81c1ed0bc3744e5a8dfdeba8239418",
  "cid": "QmV14d7ce56635a39f648257465a68dc04074a81c1ed",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292599,
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
      "evaluated_at": 1760292599
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
  "sig": "f0f69f9972135bc413628f7f9dcc46ec4bcfc55af4b8e114f5c636397f4edc88"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021479776
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 201, 'threshold': 50, 'total_amount': 46337736, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 200, 'first_seen': 1760285763, 'matching_hash': '6c002fd60c3e5dde'}}}maly': {'fraud_detected': True, 'risk_score': 89, 'details': {'zscore': 4.93, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9380590}}}