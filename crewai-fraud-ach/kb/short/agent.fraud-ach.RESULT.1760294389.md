```json
{
  "id": "9d156bd6fa2a0cc4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294389,
  "host_pid": "9e6742732c60:1",
  "hash": "ad54e1e676f96321eaee2c5bfa26466050b0eb35c580259a66aba559ae5a60e1",
  "cid": "QmV1ad54e1e676f96321eaee2c5bfa26466050b0eb35",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294389,
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
      "evaluated_at": 1760294389
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
  "sig": "de8553a0205cd9ed0c9c09c61ee73eba089c05fb115dfda17e830c7c514f12bd"
}
```

Fraud detected: amount_anomaly (score: 86)
Transaction: 021000029420003
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 1564809090, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285764, 'matching_hash': '37b4044b8dabc650'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 73, 'details': {'zscore': 3.35, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6602570}}}