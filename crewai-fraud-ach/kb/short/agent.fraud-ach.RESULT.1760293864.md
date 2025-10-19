```json
{
  "id": "4aff6eaa74cdcb55",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293864,
  "host_pid": "9e6742732c60:1",
  "hash": "5b7f3af34808641ff5e0330d079e88ae04fc3c0ac0d69c5f5a76f3470f397de2",
  "cid": "QmV15b7f3af34808641ff5e0330d079e88ae04fc3c0a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293864,
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
      "evaluated_at": 1760293864
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
  "sig": "1e11a612d5ecc0204f98e08acabdfe7acd340c0f0e61676e46a0d42095778cf3"
}
```

Fraud detected: amount_anomaly (score: 91)
Transaction: 026009598883007
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 2167013959, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285764, 'matching_hash': '3affdb087741de2d'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 90, 'details': {'zscore': 5.02, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9546317}}}