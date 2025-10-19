```json
{
  "id": "916852761e610140",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292478,
  "host_pid": "9e6742732c60:1",
  "hash": "8278ea827e07159f8da747631ab5bd9fc777187a7372955314837ef6985ae1d6",
  "cid": "QmV18278ea827e07159f8da747631ab5bd9fc777187a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292478,
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
      "evaluated_at": 1760292478
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
  "sig": "4a4a7288ce26a21e33896f10df0850bb49631ae30a5016f36b73efda1c25479d"
}
```

Fraud detected: amount_anomaly (score: 88)
Transaction: 031201467009203
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 198, 'threshold': 50, 'total_amount': 1570886856, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 197, 'first_seen': 1760285765, 'matching_hash': 'e7911512dd8ff7c4'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 81, 'details': {'zscore': 4.1, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 7933772}}}