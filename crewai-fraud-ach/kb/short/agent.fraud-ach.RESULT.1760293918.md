```json
{
  "id": "80fa0eebd8204fde",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293918,
  "host_pid": "9e6742732c60:1",
  "hash": "e9c1d84b327d2ddb4f82088ce75e3692666085b03bf13e45d802bfe7ae55e35b",
  "cid": "QmV1e9c1d84b327d2ddb4f82088ce75e3692666085b0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293918,
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
      "evaluated_at": 1760293918
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
  "sig": "79a8be6742e645e32d5258ac586a31593be6332b3e3d78176fbf6df7d43b30db"
}
```

Fraud detected: amount_anomaly (score: 89)
Transaction: 021000020489818
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 228, 'threshold': 50, 'total_amount': 1923208500, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 227, 'first_seen': 1760285765, 'matching_hash': 'b3efe19f99a87213'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 83, 'details': {'zscore': 4.39, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 8435125}}}