```json
{
  "id": "9b61bb0393a95baa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289154,
  "host_pid": "9e6742732c60:1",
  "hash": "8ee37bc1408dec4a91cb760bdf8d83cfac0d52e6ba5b3b8302fed8847586a23e",
  "cid": "QmV18ee37bc1408dec4a91cb760bdf8d83cfac0d52e6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289154,
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
      "evaluated_at": 1760289154
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
  "sig": "7a8214c6cefdb10a80447043eb5a928390a935836c2f2ba5e658f9bcc6f79d9d"
}
```

Fraud detected: amount_anomaly (score: 88)
Transaction: 021000025025802
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 115, 'threshold': 50, 'total_amount': 922107375, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 114, 'first_seen': 1760285764, 'matching_hash': 'd7be7bb127c676c6'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 81, 'details': {'zscore': 4.15, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8018325}}}