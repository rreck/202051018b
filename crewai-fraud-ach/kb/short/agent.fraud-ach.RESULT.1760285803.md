```json
{
  "id": "9e984a4c68132035",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285803,
  "host_pid": "9e6742732c60:1",
  "hash": "4331ea1e6b24bd152febca500aa1ba3152892eee15659dc01518656294d57209",
  "cid": "QmV14331ea1e6b24bd152febca500aa1ba3152892eee",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285803,
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
      "evaluated_at": 1760285803
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
  "sig": "88f96b7dd2415d1da7794f60cf05dc8b9855c7d687546e0557833ee6bf0f4f06"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201463621906
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 2, 'first_seen': 1760285763, 'matching_hash': 'c1b23d91813533f7'}}} 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 78, 'first_seen': 1760284979, 'matching_hash': 'a7542f9d69c5b02c'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 5595688}}}