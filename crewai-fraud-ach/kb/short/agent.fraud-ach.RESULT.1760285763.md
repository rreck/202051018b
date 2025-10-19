```json
{
  "id": "5e081077fdafdccf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285763,
  "host_pid": "9e6742732c60:1",
  "hash": "39754e243154ac9ea5abab1176b2cec6722cc66411114bcf9839de023ba857cb",
  "cid": "QmV139754e243154ac9ea5abab1176b2cec6722cc664",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285763,
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
      "evaluated_at": 1760285763
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "e1d41f413ed30be0b9927ea98e486e0ecc59f58e66976928862b030b35544a6f"
}
```

Fraud detected: invalid_routing (score: 95)
Transaction: 646437634699290
Details: {'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '646437635', 'validation_error': 'Invalid routing number checksum'}}}: 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 76, 'first_seen': 1760284979, 'matching_hash': 'a7542f9d69c5b02c'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 5595688}}}