```json
{
  "id": "cf6947659b365f2e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289644,
  "host_pid": "9e6742732c60:1",
  "hash": "bdae79bb598715555452b089a505f6640f023669e9a88abb7c502e7c2ea5b541",
  "cid": "QmV1bdae79bb598715555452b089a505f6640f023669",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289644,
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
      "evaluated_at": 1760289644
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
  "sig": "6b3f4b749f0d6f4c8669d6876a4cd6f20458eaa1b8346389d69b44cd01af46b3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029588067
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 129, 'threshold': 50, 'total_amount': 39702330, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 128, 'first_seen': 1760285764, 'matching_hash': '5ca8480d00f733c5'}}}