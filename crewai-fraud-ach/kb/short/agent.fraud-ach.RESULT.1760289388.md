```json
{
  "id": "9c02faa932d67b90",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289388,
  "host_pid": "9e6742732c60:1",
  "hash": "2c026615916e728c612e47ed850aa5fcb5bed65b8b6922141d01f87c2abea359",
  "cid": "QmV12c026615916e728c612e47ed850aa5fcb5bed65b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289388,
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
      "evaluated_at": 1760289388
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
  "sig": "e78a5c789cfb95c90e3a908cfcb3914bb3be0e474e0564c4b3be9d5b98662327"
}
```

Fraud detected: amount_anomaly (score: 91)
Transaction: 026009592950397
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 122, 'threshold': 50, 'total_amount': 1135413008, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 121, 'first_seen': 1760285763, 'matching_hash': '5b23ebe5172c1d5f'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 88, 'details': {'zscore': 4.89, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9306664}}}