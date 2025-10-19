```json
{
  "id": "dac09933a7341092",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292939,
  "host_pid": "9e6742732c60:1",
  "hash": "27b6c5613a9a77e9e603cd905bf9570bef5574d01dbc1a2dfda5c41420ab284b",
  "cid": "QmV127b6c5613a9a77e9e603cd905bf9570bef5574d0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292939,
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
      "evaluated_at": 1760292939
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
  "sig": "fe59b27205c206be215f0842eca324c3e7f6f950d0cdee5909a74e395d67de97"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 044000039260642
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 284, 'threshold': 50, 'total_amount': 1589175392, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 283, 'first_seen': 1760284979, 'matching_hash': 'a7542f9d69c5b02c'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 5595688}}}