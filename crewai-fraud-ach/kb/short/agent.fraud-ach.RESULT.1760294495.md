```json
{
  "id": "b8493efc1b88d246",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294495,
  "host_pid": "9e6742732c60:1",
  "hash": "ee0c59d3bf1675c66e2c5eb61edab137bdf281b7fedf6cd1d2517ff9fc1103ee",
  "cid": "QmV1ee0c59d3bf1675c66e2c5eb61edab137bdf281b7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294495,
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
      "evaluated_at": 1760294495
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
  "sig": "fd40da211f914f1e916929404151e1d865f7a98af78dfbf10ea263bca3faf74c"
}
```

Fraud detected: amount_anomaly (score: 89)
Transaction: 111000020782458
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 2054375168, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285764, 'matching_hash': '09f46afbb4d14766'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 84, 'details': {'zscore': 4.48, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 8595712}}}