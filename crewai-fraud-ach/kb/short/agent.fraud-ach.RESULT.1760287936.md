```json
{
  "id": "30becedde5c8d4ac",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287936,
  "host_pid": "9e6742732c60:1",
  "hash": "70e42ecef0e397d6c3008bc6aaad3c71a1670473db13836e62f6e5ff41b9b6fb",
  "cid": "QmV170e42ecef0e397d6c3008bc6aaad3c71a1670473",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287936,
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
      "evaluated_at": 1760287936
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
  "sig": "bf1c58e12e0c6336b3c50fce6a2a12a5dc9eb8bbf637455ff6332c4ec254ac54"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 063100279293429
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 77, 'threshold': 50, 'total_amount': 403423636, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 76, 'first_seen': 1760285763, 'matching_hash': 'f44f07036b33cc03'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 5239268}}}