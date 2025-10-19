```json
{
  "id": "b1ad6a10f17f5120",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287985,
  "host_pid": "9e6742732c60:1",
  "hash": "e6f06790e1182660db01f8497be2f0a0d7cada40f1f6fd1ac6ab3b13f268cad6",
  "cid": "QmV1e6f06790e1182660db01f8497be2f0a0d7cada40",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287985,
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
      "evaluated_at": 1760287985
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
  "sig": "d0f167b5729a31b62d99d580e6f2e92f58e21ce8ae462b3efc48c8fe20f16b1e"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 111000024041930
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 79, 'threshold': 50, 'total_amount': 581900570, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 78, 'first_seen': 1760285763, 'matching_hash': 'd0d1b4b42d54423e'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 7365830}}}