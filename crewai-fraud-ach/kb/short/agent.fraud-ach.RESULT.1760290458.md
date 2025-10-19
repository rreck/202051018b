```json
{
  "id": "213aaa65767eb211",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290458,
  "host_pid": "9e6742732c60:1",
  "hash": "5b82ef3ca38075d473fde9bdd6e0fff722c16bcff0651ed1e1daae0fb294186d",
  "cid": "QmV15b82ef3ca38075d473fde9bdd6e0fff722c16bcf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290458,
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
      "evaluated_at": 1760290458
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
  "sig": "4d03e88b494783bb924d9e486aa43f1d9fe2deb544d2a7f12ea21c1282c9829a"
}
```

Fraud detected: amount_anomaly (score: 90)
Transaction: 031201463227855
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 151, 'threshold': 50, 'total_amount': 1380842301, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 150, 'first_seen': 1760285763, 'matching_hash': 'a9c92113e6dbf136'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 87, 'details': {'zscore': 4.79, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9144651}}}