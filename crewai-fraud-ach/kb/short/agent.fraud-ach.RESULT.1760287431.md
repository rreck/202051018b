```json
{
  "id": "82de1b89b0606129",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287431,
  "host_pid": "9e6742732c60:1",
  "hash": "f7d0b3ba702ddd3881218af7f55995ff119e1879dae4651e6a3926c2e83c05d5",
  "cid": "QmV1f7d0b3ba702ddd3881218af7f55995ff119e1879",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287431,
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
      "evaluated_at": 1760287431
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_high"
  ],
  "sig": "ac2df71e7674208d42f81e385464720b12046f917237ec7d85e0d25a7dc1bc78"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 021000029533260
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 60, 'threshold': 50, 'total_amount': 481112940, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 59, 'first_seen': 1760285763, 'matching_hash': '6cc2b71c57585513'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 8018549}}}ksum'}}}