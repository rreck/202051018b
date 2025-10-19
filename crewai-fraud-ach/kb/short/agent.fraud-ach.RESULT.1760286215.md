```json
{
  "id": "e169e6ed553df432",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286215,
  "host_pid": "9e6742732c60:1",
  "hash": "8553c0067df5a21775f93f649808f51e137db6cd3a1a7dfd6d5342cdfbc5eea4",
  "cid": "QmV18553c0067df5a21775f93f649808f51e137db6cd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286215,
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
      "evaluated_at": 1760286215
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
  "sig": "43cd89905441114338b1bfa06abfea1f28e7572dc479c3c8d3fe77f31f6f6ae0"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000240116635
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 17, 'first_seen': 1760285763, 'matching_hash': 'faa8e9f78afe3726'}}}re': 85, 'details': {'duplicate_count': 17, 'first_seen': 1760285765, 'matching_hash': '9eefc6a12f8b62a3'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 7672042}}}