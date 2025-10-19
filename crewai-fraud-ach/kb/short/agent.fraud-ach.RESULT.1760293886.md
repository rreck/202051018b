```json
{
  "id": "8f610f893a0d3826",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293886,
  "host_pid": "9e6742732c60:1",
  "hash": "5630ee9e56c6b03363809e0673a32ad11fa22485cb17823ed1cebbdb90d401fa",
  "cid": "QmV15630ee9e56c6b03363809e0673a32ad11fa22485",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293886,
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
      "evaluated_at": 1760293886
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
  "sig": "6a59a62d73e19b3549861bb9a5e508baa2d35a95b3dd9a10471c7d7aa49af952"
}
```

Fraud detected: amount_anomaly (score: 90)
Transaction: 121000242247066
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 2062694520, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285765, 'matching_hash': '1251c161514af894'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 87, 'details': {'zscore': 4.76, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9086760}}}