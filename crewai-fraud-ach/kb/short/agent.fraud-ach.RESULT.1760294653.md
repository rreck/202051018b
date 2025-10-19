```json
{
  "id": "018aee394d05010a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294653,
  "host_pid": "9e6742732c60:1",
  "hash": "98758362291451b7d8b4e84b98a97bbfc49b446ac542c1afec3fbea77bb73fd6",
  "cid": "QmV198758362291451b7d8b4e84b98a97bbfc49b446a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294653,
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
      "evaluated_at": 1760294653
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
  "sig": "2df60b4dec9aaaa527c9db6f6db767ba1a7f63466382576dfc9095b3dda8ce6c"
}
```

Fraud detected: amount_anomaly (score: 91)
Transaction: 026009598883007
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 2310208714, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285764, 'matching_hash': '3affdb087741de2d'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 90, 'details': {'zscore': 5.02, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9546317}}}