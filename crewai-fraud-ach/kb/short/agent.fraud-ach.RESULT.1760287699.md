```json
{
  "id": "63f336b3e8be565a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287699,
  "host_pid": "9e6742732c60:1",
  "hash": "2db7215d3f45fcab9fc9ec550672d753a92c16bdcb006d991677a0bda0bb792d",
  "cid": "QmV12db7215d3f45fcab9fc9ec550672d753a92c16bd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287699,
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
      "evaluated_at": 1760287699
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_high"
  ],
  "sig": "3d66c64bca9ba4b6516008ef8fc95f539f321c2c35c2b02d84466e8f6d1f6510"
}
```

Fraud detected: amount_anomaly (score: 77)
Transaction: 031201464331888
Details: {'velocity': {'fraud_detected': True, 'risk_score': 88, 'details': {'transaction_count': 69, 'threshold': 50, 'total_amount': 436960923, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 68, 'first_seen': 1760285764, 'matching_hash': '6a7d940bcd4512ca'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6332767}}}