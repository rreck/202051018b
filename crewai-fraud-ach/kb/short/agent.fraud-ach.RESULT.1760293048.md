```json
{
  "id": "ff68eddd10762788",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293048,
  "host_pid": "9e6742732c60:1",
  "hash": "575792bcbb2885dfefb89092bbfd6a03b315b623acb92e8c7b0aa517e5801e62",
  "cid": "QmV1575792bcbb2885dfefb89092bbfd6a03b315b623",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293048,
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
      "evaluated_at": 1760293048
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
  "sig": "663afe6fb3462d5598c3ed1e65e5e99104c8d6ada4b5270929233fa9262bd623"
}
```

Fraud detected: amount_anomaly (score: 88)
Transaction: 031201467009203
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 210, 'threshold': 50, 'total_amount': 1666092120, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 209, 'first_seen': 1760285765, 'matching_hash': 'e7911512dd8ff7c4'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 81, 'details': {'zscore': 4.1, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 7933772}}}