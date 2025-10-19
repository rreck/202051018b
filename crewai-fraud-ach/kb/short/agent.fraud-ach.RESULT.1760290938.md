```json
{
  "id": "8b169e282b59b6ee",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290938,
  "host_pid": "9e6742732c60:1",
  "hash": "a7bf83e637e841f870fd6ff60da9e87308121e5756822dd363ef70c70d4c80f7",
  "cid": "QmV1a7bf83e637e841f870fd6ff60da9e87308121e57",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290938,
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
      "evaluated_at": 1760290938
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
  "sig": "42c745101c9913ee5fcced29267f74c9e3d38e869fc600da9a8fa7af69efed45"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596829725
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 163, 'threshold': 50, 'total_amount': 53865632, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 162, 'first_seen': 1760285763, 'matching_hash': '14fa64c7f7d5a53d'}}}maly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.51, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6888614}}}