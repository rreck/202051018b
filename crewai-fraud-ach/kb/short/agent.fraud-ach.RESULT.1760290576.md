```json
{
  "id": "d4441d30b5582b6f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290576,
  "host_pid": "9e6742732c60:1",
  "hash": "22f878647de2c134ae24e962d53c93276402a7ae542342d4ca96892ad0c1d3aa",
  "cid": "QmV122f878647de2c134ae24e962d53c93276402a7ae",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290576,
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
      "evaluated_at": 1760290576
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
  "sig": "6bcb6196e5110c5780a9029652a39222377fc31fc21c60b848378287e180d6c2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022691878
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 154, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 153, 'first_seen': 1760285763, 'matching_hash': 'a2c26d052e86193d'}}}5763, 'matching_hash': '7583721e7662209c'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 79, 'details': {'zscore': 3.97, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7694908}}}