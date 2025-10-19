```json
{
  "id": "855e881fac16f564",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288343,
  "host_pid": "9e6742732c60:1",
  "hash": "3193ea668deaf01600bf553ec93d32c1b62035596a9491dd545dcc06a2bf7e7b",
  "cid": "QmV13193ea668deaf01600bf553ec93d32c1b6203559",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288343,
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
      "evaluated_at": 1760288343
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
  "sig": "7873bd67ac6bfae3caf8595817c5985032532cde2740a9d3c6cf3e9057bc6875"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 121000240089409
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 90, 'threshold': 50, 'total_amount': 552512700, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 89, 'first_seen': 1760285765, 'matching_hash': 'a79d0bf31de09717'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6139030}}}