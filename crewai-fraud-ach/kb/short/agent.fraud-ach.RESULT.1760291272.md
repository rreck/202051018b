```json
{
  "id": "66b96fda2a28cbc3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291272,
  "host_pid": "9e6742732c60:1",
  "hash": "011895d0d8f605adef0b425d1485841fc6ef59239e290f2794932328537d82c9",
  "cid": "QmV1011895d0d8f605adef0b425d1485841fc6ef5923",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291272,
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
      "evaluated_at": 1760291272
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
  "sig": "62190b2037783d5c279c07b6706eb1b23c359e6f1a055373884b544971dc3ad7"
}
```

Fraud detected: amount_anomaly (score: 89)
Transaction: 111000020782458
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 171, 'threshold': 50, 'total_amount': 1469866752, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 170, 'first_seen': 1760285764, 'matching_hash': '09f46afbb4d14766'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 84, 'details': {'zscore': 4.48, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8595712}}}