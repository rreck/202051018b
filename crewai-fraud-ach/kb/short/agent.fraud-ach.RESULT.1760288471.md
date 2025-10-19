```json
{
  "id": "dc166182b067c0ed",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288471,
  "host_pid": "9e6742732c60:1",
  "hash": "bf85e4990b9bfeb5e2032151567654edd808cf7b43df5e439c6f63ef3f074058",
  "cid": "QmV1bf85e4990b9bfeb5e2032151567654edd808cf7b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288471,
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
      "evaluated_at": 1760288471
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
  "sig": "59094196565bc08e0ceb8d5d10923ccba4836bc1a2bb30db5824ed0d3096112a"
}
```

Fraud detected: amount_anomaly (score: 86)
Transaction: 121000242247066
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 94, 'threshold': 50, 'total_amount': 854155440, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 93, 'first_seen': 1760285765, 'matching_hash': '1251c161514af894'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 74, 'details': {'zscore': 3.43, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9086760}}}