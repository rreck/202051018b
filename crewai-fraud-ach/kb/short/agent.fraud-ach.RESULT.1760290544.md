```json
{
  "id": "550801dde2ed3ff1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290544,
  "host_pid": "9e6742732c60:1",
  "hash": "dab7a7feabac9c91e73b75dfa58acbea994e743f05a5f5125fffd4749e318a5c",
  "cid": "QmV1dab7a7feabac9c91e73b75dfa58acbea994e743f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290544,
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
      "evaluated_at": 1760290544
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
  "sig": "ee8bd1de0c450910a65df78a7e59009ab37e368f2b7d9d79932cc27d7c87644a"
}
```

Fraud detected: amount_anomaly (score: 89)
Transaction: 021000020489818
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 153, 'threshold': 50, 'total_amount': 1290574125, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 152, 'first_seen': 1760285765, 'matching_hash': 'b3efe19f99a87213'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 83, 'details': {'zscore': 4.39, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8435125}}}