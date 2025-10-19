```json
{
  "id": "1dc7cb4b69ba61fa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289693,
  "host_pid": "9e6742732c60:1",
  "hash": "8cda52f634234a306a5ef972c5025d5f75c9acabd4a18a26bdf2913126e19941",
  "cid": "QmV18cda52f634234a306a5ef972c5025d5f75c9acab",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289693,
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
      "evaluated_at": 1760289693
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
  "sig": "29d6f4cd12330dfab0b8e105eb358fb6f3c30f95a21b09f99a4379a42c1b6864"
}
```

Fraud detected: amount_anomaly (score: 91)
Transaction: 063100275758456
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 130, 'threshold': 50, 'total_amount': 1224229370, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 129, 'first_seen': 1760285765, 'matching_hash': 'e3feb2a34db32d71'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 89, 'details': {'zscore': 4.95, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9417149}}}