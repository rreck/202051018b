```json
{
  "id": "1d53129bc43765e2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292337,
  "host_pid": "9e6742732c60:1",
  "hash": "dc6f795afe35668523459c84e5409a79d9a33e5947ea193b1db6c57edf7de1a6",
  "cid": "QmV1dc6f795afe35668523459c84e5409a79d9a33e59",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292337,
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
      "evaluated_at": 1760292337
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
  "sig": "87372f6296024041c6a1cd14895f0d2117a4244e16f6cf7f08998f6c00cf555c"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 063100275328879
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 195, 'threshold': 50, 'total_amount': 1092921570, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 194, 'first_seen': 1760285764, 'matching_hash': '9f5415d10b328afc'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 5604726}}}