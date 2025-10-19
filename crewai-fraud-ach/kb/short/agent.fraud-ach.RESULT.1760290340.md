```json
{
  "id": "a821c4b8e9c434a6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290340,
  "host_pid": "9e6742732c60:1",
  "hash": "f1b49c042ecb39aba707e90a1dfaf923700dad4611cca10a40f935d11b0a7921",
  "cid": "QmV1f1b49c042ecb39aba707e90a1dfaf923700dad46",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290340,
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
      "evaluated_at": 1760290341
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
  "sig": "ce0ff8473f7663c64cfce5f28f01b76f053ba533f12b48387383feae761f41ee"
}
```

Fraud detected: amount_anomaly (score: 91)
Transaction: 026009592950397
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 148, 'threshold': 50, 'total_amount': 1377386272, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 147, 'first_seen': 1760285763, 'matching_hash': '5b23ebe5172c1d5f'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 88, 'details': {'zscore': 4.89, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9306664}}}