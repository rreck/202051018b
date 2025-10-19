```json
{
  "id": "e4eaefb7dab61f4d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285969,
  "host_pid": "9e6742732c60:1",
  "hash": "19f57b537a699a4cb36dc727eeb6407bd46b042512a0d9dcd4d67622a1767cb6",
  "cid": "QmV119f57b537a699a4cb36dc727eeb6407bd46b0425",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285969,
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
      "evaluated_at": 1760285969
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
  "sig": "8b87bafea51383ec3f32a001195ef3ce5a5121bec26a6d9b4e083e470962540f"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201461090276
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 9, 'first_seen': 1760285763, 'matching_hash': '697ecd0ef10c625b'}}}re': 85, 'details': {'duplicate_count': 9, 'first_seen': 1760285763, 'matching_hash': '91e9478c27780a65'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6875376}}}