```json
{
  "id": "965490807957c09e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288263,
  "host_pid": "9e6742732c60:1",
  "hash": "67309b0ef258e498a845f6818fdf73cd489088ab4e49fba72246b0321c7e011b",
  "cid": "QmV167309b0ef258e498a845f6818fdf73cd489088ab",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288263,
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
      "evaluated_at": 1760288263
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
  "sig": "dc5b1e9971e5cc8553cdc5e8fe23c276e9bae685de81c9832d873468d48c42b4"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 021000021703881
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 88, 'threshold': 50, 'total_amount': 568956960, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 87, 'first_seen': 1760285763, 'matching_hash': '20cca8b4db3b5ffd'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6465420}}}