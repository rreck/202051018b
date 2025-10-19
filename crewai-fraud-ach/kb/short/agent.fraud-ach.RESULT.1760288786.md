```json
{
  "id": "2a404efeda411d3f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288786,
  "host_pid": "9e6742732c60:1",
  "hash": "23a55fa37add984fc9c31e6cb35958dc358135953d31ac752c5e7673f5fa6732",
  "cid": "QmV123a55fa37add984fc9c31e6cb35958dc35813595",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288786,
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
      "evaluated_at": 1760288786
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
  "sig": "ab7ea406e8c3f89956acf8d37d146d0f847a5495601a1863b395499c96f9e6a3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023973780
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 104, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 103, 'first_seen': 1760285763, 'matching_hash': 'a6cf7acef53d66c2'}}}764, 'matching_hash': 'ca8349fc21f82b4d'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.51, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6888614}}}