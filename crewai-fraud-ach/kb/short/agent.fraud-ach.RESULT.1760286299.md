```json
{
  "id": "c36d2ad0d6777e87",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286299,
  "host_pid": "9e6742732c60:1",
  "hash": "c98aff50ca17e7522950151a0464653dcb4d213d57393bd6c98ceb797bd3bac7",
  "cid": "QmV1c98aff50ca17e7522950151a0464653dcb4d213d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286299,
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
      "evaluated_at": 1760286299
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
  "sig": "8fa6e8e7c57bb77a63c8385d047c5d9f89a1212c98ec84e7868907ac241233bc"
}
```

Fraud detected: amount_anomaly (score: 77)
Transaction: 021000021072241
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 202775181, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 20, 'first_seen': 1760285763, 'matching_hash': 'ac02650f27bf80d6'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 76, 'details': {'zscore': 3.69, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9655961}}}