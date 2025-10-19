```json
{
  "id": "ddbf66543210e49e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290277,
  "host_pid": "9e6742732c60:1",
  "hash": "796f487547e9b8451fcf968e55c63c9d4a418144fd72af707262084dbe22f92e",
  "cid": "QmV1796f487547e9b8451fcf968e55c63c9d4a418144",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290277,
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
      "evaluated_at": 1760290277
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "cefd213a538a1d1ea38ab7d9c66f751a8b1e71a7d71a16a3a6c2316569c8d0c0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272098114
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 146, 'threshold': 50, 'total_amount': 60509846, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 145, 'first_seen': 1760285764, 'matching_hash': '010bb0d7cfc5cc6e'}}}unt_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}