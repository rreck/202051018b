```json
{
  "id": "830a31659d2c3ab6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293516,
  "host_pid": "9e6742732c60:1",
  "hash": "1994af4d292c1c7164091747583c60e89e3e4d9a4e6e2a4a80c86ffcde6ce032",
  "cid": "QmV11994af4d292c1c7164091747583c60e89e3e4d9a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293516,
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
      "evaluated_at": 1760293516
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
  "sig": "dee9bcaeb930a8bb12c5b3c999f6bf14d08252818ef57378c449cf60d331ec72"
}
```

Fraud detected: amount_anomaly (score: 89)
Transaction: 021000020489818
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 220, 'threshold': 50, 'total_amount': 1855727500, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 219, 'first_seen': 1760285765, 'matching_hash': 'b3efe19f99a87213'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 83, 'details': {'zscore': 4.39, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 8435125}}}