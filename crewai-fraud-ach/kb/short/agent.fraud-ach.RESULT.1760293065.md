```json
{
  "id": "add10dc7203b6958",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293065,
  "host_pid": "9e6742732c60:1",
  "hash": "901c3b8b752e046003fefd0bf26b8ae0905b05f8f6b9e3971a346560875a0be9",
  "cid": "QmV1901c3b8b752e046003fefd0bf26b8ae0905b05f8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293065,
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
      "evaluated_at": 1760293065
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
  "sig": "743daa859efcae22e67aa8e4431cece35eb962b47ef5d9a722ba9a0673876d0b"
}
```

Fraud detected: amount_anomaly (score: 90)
Transaction: 121000241645883
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 211, 'threshold': 50, 'total_amount': 1841175028, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 210, 'first_seen': 1760285763, 'matching_hash': '8711cb2fb2144ae4'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 85, 'details': {'zscore': 4.56, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 8725948}}}