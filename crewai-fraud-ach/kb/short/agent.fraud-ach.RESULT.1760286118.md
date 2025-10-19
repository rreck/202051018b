```json
{
  "id": "b60f4cc02f5f940f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286118,
  "host_pid": "9e6742732c60:1",
  "hash": "0c0654899e0f157e35924a5f83d1ba4c30657c4d44b6b391540b23a5e6c23ab4",
  "cid": "QmV10c0654899e0f157e35924a5f83d1ba4c30657c4d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286118,
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
      "evaluated_at": 1760286118
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "7e64e1ff3a6c50c6dee239ba0e6321920a7a5391a0d3c391501d79a4475dc360"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100273476886
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 14, 'first_seen': 1760285763, 'matching_hash': 'e52038f69d26fe5a'}}}re': 85, 'details': {'duplicate_count': 14, 'first_seen': 1760285763, 'matching_hash': '7583721e7662209c'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 7694908}}}