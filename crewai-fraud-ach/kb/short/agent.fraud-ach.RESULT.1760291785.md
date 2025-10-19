```json
{
  "id": "9080ed69ecf7221b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291785,
  "host_pid": "9e6742732c60:1",
  "hash": "75e99fb9ac28558dabac2d78d05dc7289c073673c7dc030b4e79beacb9656e90",
  "cid": "QmV175e99fb9ac28558dabac2d78d05dc7289c073673",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291785,
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
      "evaluated_at": 1760291785
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
  "sig": "24daf79ecd453bd4c28089bd944f174a580964c344b2efa095153647f20fd1b0"
}
```

Fraud detected: amount_anomaly (score: 91)
Transaction: 063100270473682
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 183, 'threshold': 50, 'total_amount': 1747211715, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 182, 'first_seen': 1760285763, 'matching_hash': 'dcfb2900505c6ddc'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 90, 'details': {'zscore': 5.02, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9547605}}}