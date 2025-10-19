```json
{
  "id": "3f1a66bbb7c29e84",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286467,
  "host_pid": "9e6742732c60:1",
  "hash": "297252f0ff8075ebf30071cc9c8f66213bab980c5d69928e3e303481ba32baeb",
  "cid": "QmV1297252f0ff8075ebf30071cc9c8f66213bab980c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286467,
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
      "evaluated_at": 1760286467
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_high"
  ],
  "sig": "52d84425c6946bcc2cbf206b9dc2e2ebc9ce531ee843e845104d7f4e869f8f1f"
}
```

Fraud detected: amount_anomaly (score: 76)
Transaction: 026009597367941
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 241958756, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 25, 'first_seen': 1760285764, 'matching_hash': '5430161f1ba10767'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.53, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9306106}}}