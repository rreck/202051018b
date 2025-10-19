```json
{
  "id": "b974699ba42563d1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293852,
  "host_pid": "9e6742732c60:1",
  "hash": "56cf00a6e66b8f965c0d89e6f02711df52ada089cfe128e8db631e3962db4af7",
  "cid": "QmV156cf00a6e66b8f965c0d89e6f02711df52ada089",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293852,
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
      "evaluated_at": 1760293852
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
  "sig": "aee3048eb5914d9cfeb49af9fcee954505b0dcb681584ccf842e2cca5897750a"
}
```

Fraud detected: amount_anomaly (score: 86)
Transaction: 026009599754451
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 1512796554, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285763, 'matching_hash': '546a5bdf8e1b6fa5'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 73, 'details': {'zscore': 3.38, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6664302}}}