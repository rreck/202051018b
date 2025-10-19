```json
{
  "id": "680d2ad016db6923",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287382,
  "host_pid": "9e6742732c60:1",
  "hash": "8fd0d84394f33c6395a3986aa3681ded68d726bbc9d82504dfd21b963e0b5f01",
  "cid": "QmV18fd0d84394f33c6395a3986aa3681ded68d726bb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287382,
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
      "evaluated_at": 1760287382
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
  "sig": "b2dc8648fd8e8c414d3eddd859f87904112886e15bbd858b933fc2f597b165fe"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 122105155421893
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 58, 'threshold': 50, 'total_amount': 293638166, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 57, 'first_seen': 1760285765, 'matching_hash': 'b50b947262955843'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 5062727}}}