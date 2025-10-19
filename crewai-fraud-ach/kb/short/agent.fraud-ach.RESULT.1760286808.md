```json
{
  "id": "d5a479ebc0bc788f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286808,
  "host_pid": "9e6742732c60:1",
  "hash": "ea40df262d50b8c796373b4f5edab5fb2e209c6127a90c6d2845ebe0afb94f94",
  "cid": "QmV1ea40df262d50b8c796373b4f5edab5fb2e209c61",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286808,
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
      "evaluated_at": 1760286808
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
  "sig": "b2922f4c57ed46c0b823fab26d468106e1e80ae1677025c2bb2f268e8ca87625"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201469028209
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 37, 'first_seen': 1760285763, 'matching_hash': 'a4269a968e85dafe'}}}re': 85, 'details': {'duplicate_count': 37, 'first_seen': 1760285763, 'matching_hash': '9c4bf7694cd7e546'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 5035466}}}