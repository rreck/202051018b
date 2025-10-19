```json
{
  "id": "3caa280b2e1e397f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288949,
  "host_pid": "9e6742732c60:1",
  "hash": "2a78e37243d311e7b625f6ad0d2f59766d8a95904f90da29ffe466e7154720f2",
  "cid": "QmV12a78e37243d311e7b625f6ad0d2f59766d8a9590",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288949,
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
      "evaluated_at": 1760288949
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
  "sig": "94a5b3a39812524a7ecdec8437527768a5d9cc4109df19cc37aba6b4dd740733"
}
```

Fraud detected: amount_anomaly (score: 87)
Transaction: 122105154811722
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 109, 'threshold': 50, 'total_amount': 816811120, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 108, 'first_seen': 1760285763, 'matching_hash': 'f2f6645498600029'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 78, 'details': {'zscore': 3.85, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7493680}}}