```json
{
  "id": "b8842ab0cbedc5db",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287866,
  "host_pid": "9e6742732c60:1",
  "hash": "d461d0a3e959284b1b495903ea12aba66f64f47a846d7b5bf9e0482c5af275f7",
  "cid": "QmV1d461d0a3e959284b1b495903ea12aba66f64f47a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287866,
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
      "evaluated_at": 1760287866
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
  "sig": "31bc3c40cbba6685fb927d5c3fcaa15d996e409b1b5e86cf5f17278035f67f2f"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 122105154811722
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 75, 'threshold': 50, 'total_amount': 562026000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 74, 'first_seen': 1760285763, 'matching_hash': 'f2f6645498600029'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 7493680}}}