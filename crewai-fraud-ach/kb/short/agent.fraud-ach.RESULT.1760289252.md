```json
{
  "id": "ed551c878cceb73d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289252,
  "host_pid": "9e6742732c60:1",
  "hash": "852a5074b63d0f9a57b2e02d5d78e8fae10ce7f24edd66a2fb3429c844ab3dfa",
  "cid": "QmV1852a5074b63d0f9a57b2e02d5d78e8fae10ce7f2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289252,
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
      "evaluated_at": 1760289252
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
  "sig": "8da5c506558ec4bc36195a9dbe2d6829ee32836a8fc3cc31e8a02993529a9ec8"
}
```

Fraud detected: amount_anomaly (score: 87)
Transaction: 021000024856185
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 118, 'threshold': 50, 'total_amount': 844517622, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 117, 'first_seen': 1760285763, 'matching_hash': '03b6a41c39a9a2ab'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 76, 'details': {'zscore': 3.66, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7156929}}}