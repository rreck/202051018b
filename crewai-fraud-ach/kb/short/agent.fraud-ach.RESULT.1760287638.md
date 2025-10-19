```json
{
  "id": "f0fe1643108d24c1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287638,
  "host_pid": "9e6742732c60:1",
  "hash": "d8eb49094a5f6862f47225adb230618fd0ae6028a443ca23b3dcabaa2ccb762b",
  "cid": "QmV1d8eb49094a5f6862f47225adb230618fd0ae6028",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287638,
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
      "evaluated_at": 1760287638
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
  "sig": "251c6b0394f27c4a7fed9d7d851098ab5091ee3a9a89dfcb0436deed14c469e3"
}
```

Fraud detected: amount_anomaly (score: 79)
Transaction: 122105150198952
Details: {'velocity': {'fraud_detected': True, 'risk_score': 84, 'details': {'transaction_count': 67, 'threshold': 50, 'total_amount': 558406542, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 66, 'first_seen': 1760285763, 'matching_hash': '35a36fb353493cca'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 70, 'details': {'zscore': 3.1, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 8334426}}}