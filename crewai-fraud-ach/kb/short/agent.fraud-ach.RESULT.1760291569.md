```json
{
  "id": "e496330a3212c841",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291569,
  "host_pid": "9e6742732c60:1",
  "hash": "4f15842b12915cd661ebdd3687dc3489ff20fadb7503e9b7762823ba057c3bc9",
  "cid": "QmV14f15842b12915cd661ebdd3687dc3489ff20fadb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291569,
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
      "evaluated_at": 1760291569
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
  "sig": "1563c79d982d1f5ef94ce7fc2cfaa455e95b27ca10649d5475d6052fa8dc7d04"
}
```

Fraud detected: amount_anomaly (score: 91)
Transaction: 111000022658248
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 178, 'threshold': 50, 'total_amount': 1669745020, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 177, 'first_seen': 1760285764, 'matching_hash': '6b9326523c35dc7b'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 89, 'details': {'zscore': 4.93, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9380590}}}