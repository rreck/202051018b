```json
{
  "id": "b0d38205ae210093",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288220,
  "host_pid": "9e6742732c60:1",
  "hash": "416a8a3931513f566e5d236e0af7ca2e0adcf5b5c168e058d3247093864f4379",
  "cid": "QmV1416a8a3931513f566e5d236e0af7ca2e0adcf5b5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288220,
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
      "evaluated_at": 1760288220
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
  "sig": "0d9b904bc94d8ce23e4eea5a9b12d3e91c32fd5273b738ab828ae7e44a8994c8"
}
```

Fraud detected: amount_anomaly (score: 87)
Transaction: 021000026914318
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 86, 'threshold': 50, 'total_amount': 841397340, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 85, 'first_seen': 1760285765, 'matching_hash': '634436741ef501a5'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 77, 'details': {'zscore': 3.75, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9783690}}}