```json
{
  "id": "eaef787ea0472ad5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293208,
  "host_pid": "9e6742732c60:1",
  "hash": "c5f1d5f000094e06faa4849eb94ba26ff1246b71468b112a39cb377ad8a6a73b",
  "cid": "QmV1c5f1d5f000094e06faa4849eb94ba26ff1246b71",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293208,
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
      "evaluated_at": 1760293208
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
  "sig": "fa32b6b0946334b98efa5ebbc0218bf829b6d75c7b21ada13f6a4330c7060df7"
}
```

Fraud detected: amount_anomaly (score: 85)
Transaction: 021000021703881
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 214, 'threshold': 50, 'total_amount': 1383599880, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 213, 'first_seen': 1760285763, 'matching_hash': '20cca8b4db3b5ffd'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 72, 'details': {'zscore': 3.27, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6465420}}}