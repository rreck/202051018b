```json
{
  "id": "e3be42f2e97ec7e5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290496,
  "host_pid": "9e6742732c60:1",
  "hash": "5264b69cda9c18663cf938e034f6c6ddbaed6b0da4456b8c80d39ea33690f0ae",
  "cid": "QmV15264b69cda9c18663cf938e034f6c6ddbaed6b0d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290496,
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
      "evaluated_at": 1760290496
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
  "sig": "f6e1618112ef5b91e9e239967c259de3dad3f93f1113b19be8b1faee8786fd47"
}
```

Fraud detected: amount_anomaly (score: 88)
Transaction: 021000029533260
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 152, 'threshold': 50, 'total_amount': 1218819448, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 151, 'first_seen': 1760285763, 'matching_hash': '6cc2b71c57585513'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 81, 'details': {'zscore': 4.15, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8018549}}}