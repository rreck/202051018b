```json
{
  "id": "e5e105e6644c10b9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287958,
  "host_pid": "9e6742732c60:1",
  "hash": "9e9436d0102084011509a09c047bdfb1eac36403b75ba8de89bee347ebce9cb7",
  "cid": "QmV19e9436d0102084011509a09c047bdfb1eac36403",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287958,
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
      "evaluated_at": 1760287958
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
  "sig": "258a0b250de13a041e4737a2d717da7a90f64e8b3757981203b9ff7e409daa48"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 063100277645862
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 78, 'threshold': 50, 'total_amount': 507892710, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 77, 'first_seen': 1760285764, 'matching_hash': 'c7c729dc286039c9'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6511445}}}