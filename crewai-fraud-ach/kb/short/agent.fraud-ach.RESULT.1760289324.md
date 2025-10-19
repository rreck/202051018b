```json
{
  "id": "666f9145d629a449",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289324,
  "host_pid": "9e6742732c60:1",
  "hash": "3e86aca4730e4263b17ba90bc1f325a992a73f016913dca7be475b90f1aaacdf",
  "cid": "QmV13e86aca4730e4263b17ba90bc1f325a992a73f01",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289324,
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
      "evaluated_at": 1760289324
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
  "sig": "5dd6fc594aa801569655d9d27983173edb27dc7d20ba9341c3570f148be22f47"
}
```

Fraud detected: amount_anomaly (score: 86)
Transaction: 031201465557479
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 120, 'threshold': 50, 'total_amount': 799891200, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 119, 'first_seen': 1760285764, 'matching_hash': '962c9a9fec8a4a1a'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 73, 'details': {'zscore': 3.38, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6665760}}}