```json
{
  "id": "9fbb27036e098bc3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293016,
  "host_pid": "9e6742732c60:1",
  "hash": "695ffed33fb8544ac3114ca10249dadae363269d4213ab45c7157e19d20c4186",
  "cid": "QmV1695ffed33fb8544ac3114ca10249dadae363269d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293016,
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
      "evaluated_at": 1760293016
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
  "sig": "39a3cb9c983ce33c7c2cfca6ad321371f2ebeea987e09abd122f552279351c27"
}
```

Fraud detected: amount_anomaly (score: 87)
Transaction: 111000024041930
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 210, 'threshold': 50, 'total_amount': 1546824300, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 209, 'first_seen': 1760285763, 'matching_hash': 'd0d1b4b42d54423e'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 77, 'details': {'zscore': 3.78, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 7365830}}}