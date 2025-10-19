```json
{
  "id": "3f68ebf1026173c8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290795,
  "host_pid": "9e6742732c60:1",
  "hash": "ac2d4686a20460c19891a404797cdc2640b801fdaeab1848d8b3dedd30465b3d",
  "cid": "QmV1ac2d4686a20460c19891a404797cdc2640b801fd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290795,
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
      "evaluated_at": 1760290795
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
  "sig": "7da749e9e5816624da92ec3fe99f0c95a68641fa364907f3aeedaecda20e1164"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 111000026237439
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 159, 'threshold': 50, 'total_amount': 868478193, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 158, 'first_seen': 1760285765, 'matching_hash': '88704d1e07f02084'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 5462127}}}