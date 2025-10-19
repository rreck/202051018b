```json
{
  "id": "3b2e0788486b8614",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294038,
  "host_pid": "9e6742732c60:1",
  "hash": "41fb031e185390de8a444edaa2440bfe03b23855bd85a5a61e17fb98ffefbcc1",
  "cid": "QmV141fb031e185390de8a444edaa2440bfe03b23855",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294038,
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
      "evaluated_at": 1760294038
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
  "sig": "58e728a82d22b41fc9560ca3a17742dce2fe5e2b81fa6d25dd98735941ec6808"
}
```

Fraud detected: amount_anomaly (score: 91)
Transaction: 026009597367941
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 2140404380, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285764, 'matching_hash': '5430161f1ba10767'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 88, 'details': {'zscore': 4.89, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9306106}}}