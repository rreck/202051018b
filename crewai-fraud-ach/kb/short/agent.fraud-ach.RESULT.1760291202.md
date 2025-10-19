```json
{
  "id": "d1edbdfb080d6513",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291202,
  "host_pid": "9e6742732c60:1",
  "hash": "4265f933a8e0d84203910e309b54b4a8467fc2849e52072eb8b6f2f868550f57",
  "cid": "QmV14265f933a8e0d84203910e309b54b4a8467fc284",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291202,
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
      "evaluated_at": 1760291202
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
  "sig": "d4ef63dc4af1fe92ab8e41e87d139f64c81c493fd17702a97216641111a61703"
}
```

Fraud detected: amount_anomaly (score: 88)
Transaction: 121000242463666
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 169, 'threshold': 50, 'total_amount': 1320782827, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 168, 'first_seen': 1760285764, 'matching_hash': '3cd63f27035973d0'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 80, 'details': {'zscore': 4.04, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7815283}}}