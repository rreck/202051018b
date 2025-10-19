```json
{
  "id": "4e7a54cc788ddee8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290832,
  "host_pid": "9e6742732c60:1",
  "hash": "4e5ac4f9c45aec114b4de300334a1aaf75e4b7017148c1b04e10897b69ce4cab",
  "cid": "QmV14e5ac4f9c45aec114b4de300334a1aaf75e4b701",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290832,
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
      "evaluated_at": 1760290832
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
  "sig": "5e07df8f4c9d4f4b7c60583ecde3a57ae6cde936c72e901e5d6756123731c5d8"
}
```

Fraud detected: amount_anomaly (score: 88)
Transaction: 122105153391998
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 160, 'threshold': 50, 'total_amount': 1242346560, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 159, 'first_seen': 1760285764, 'matching_hash': '05c5de8ca533802c'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 80, 'details': {'zscore': 4.01, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7764666}}}