```json
{
  "id": "993df9e5917a3978",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289410,
  "host_pid": "9e6742732c60:1",
  "hash": "ff941b93f56af302093b59bb62b57760a651f74b5b729c7b58c9ca158747120c",
  "cid": "QmV1ff941b93f56af302093b59bb62b57760a651f74b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289410,
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
      "evaluated_at": 1760289410
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
  "sig": "ed4982879541a24acaaf87f3f9f78563545ef5934e26699de6d1125cf2b09482"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599905929
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 122, 'threshold': 50, 'total_amount': 47393340, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 121, 'first_seen': 1760285765, 'matching_hash': 'da08c58383816f07'}}}