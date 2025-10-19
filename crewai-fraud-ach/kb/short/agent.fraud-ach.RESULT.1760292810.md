```json
{
  "id": "9c9f140b547017dc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292810,
  "host_pid": "9e6742732c60:1",
  "hash": "1a5eeddee032b0c220ef90c42f2c6b715393011e277a9e5654a7b25c2d8307c8",
  "cid": "QmV11a5eeddee032b0c220ef90c42f2c6b715393011e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292810,
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
      "evaluated_at": 1760292810
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
  "sig": "eeaec720bdc24978ec7936fdca76c6416b55d1c649b0c744b78d312658fa67af"
}
```

Fraud detected: amount_anomaly (score: 92)
Transaction: 021000026914318
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 205, 'threshold': 50, 'total_amount': 2005656450, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 204, 'first_seen': 1760285765, 'matching_hash': '634436741ef501a5'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 91, 'details': {'zscore': 5.16, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9783690}}}