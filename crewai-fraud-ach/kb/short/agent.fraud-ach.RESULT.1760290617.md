```json
{
  "id": "639982c296c2869c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290617,
  "host_pid": "9e6742732c60:1",
  "hash": "a60857470e42be0d7ba2acac4d9f5015d9d0980700f792e2bd47f869637e7d62",
  "cid": "QmV1a60857470e42be0d7ba2acac4d9f5015d9d09807",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290617,
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
      "evaluated_at": 1760290617
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
  "sig": "2f51a43237c381214e2ed8fc8e5b0502216c0270e53a8a7bf7502f6b19f969d6"
}
```

Fraud detected: amount_anomaly (score: 91)
Transaction: 111000023855884
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 155, 'threshold': 50, 'total_amount': 1458687795, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 154, 'first_seen': 1760285763, 'matching_hash': '29f4fac8ca9c8442'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 89, 'details': {'zscore': 4.94, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9410889}}}