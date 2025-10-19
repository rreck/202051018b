```json
{
  "id": "63701eff98671e7f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288500,
  "host_pid": "9e6742732c60:1",
  "hash": "84766e4e17506638174fe331b17c5fd714412854f9701182ddab265f5ea2429f",
  "cid": "QmV184766e4e17506638174fe331b17c5fd714412854",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288500,
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
      "evaluated_at": 1760288500
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
  "sig": "edcee04b21a451734383bca10b9abd3e9dcd3f2eac2365792be0ca76410c8cc0"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 031201462394531
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 95, 'threshold': 50, 'total_amount': 725521650, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 94, 'first_seen': 1760285763, 'matching_hash': '046e1c7f2d74b138'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 7637070}}}