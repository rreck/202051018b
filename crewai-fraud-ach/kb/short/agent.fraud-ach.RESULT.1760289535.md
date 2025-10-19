```json
{
  "id": "7816a7629019c75c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289535,
  "host_pid": "9e6742732c60:1",
  "hash": "f13f3549001803a5f8d4e75d6072cdd90d05ece99b0a6304c7633b9e673b493a",
  "cid": "QmV1f13f3549001803a5f8d4e75d6072cdd90d05ece9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289535,
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
      "evaluated_at": 1760289535
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
  "sig": "2ac35798c19c382c5e56108e05bfdcae02af6ff7294694ecf5f63c41540059be"
}
```

Fraud detected: amount_anomaly (score: 91)
Transaction: 044000032483239
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 126, 'threshold': 50, 'total_amount': 1164911706, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 125, 'first_seen': 1760285764, 'matching_hash': '7bd2e976d6ef9e3c'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 88, 'details': {'zscore': 4.85, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9245331}}}