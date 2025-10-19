```json
{
  "id": "41cd3cd055e21c1d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287718,
  "host_pid": "9e6742732c60:1",
  "hash": "1af5ba37a09799cc506079961a05313c911895f0c8acf6677aa111931597e5e3",
  "cid": "QmV11af5ba37a09799cc506079961a05313c911895f0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287718,
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
      "evaluated_at": 1760287718
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
  "sig": "9e52b315534be3e80459264dae9ed2c995ebf870312a7d2e3c80f33249305f25"
}
```

Fraud detected: duplicate_transaction (score: 87)
Transaction: 031201465523405
Details: {'velocity': {'fraud_detected': True, 'risk_score': 90, 'details': {'transaction_count': 70, 'threshold': 50, 'total_amount': 20487810, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 69, 'first_seen': 1760285764, 'matching_hash': '5adc701fe9b49cb3'}}}aly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.58, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9410889}}}