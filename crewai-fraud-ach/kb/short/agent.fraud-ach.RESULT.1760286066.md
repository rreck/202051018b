```json
{
  "id": "aee6d791582e4763",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286066,
  "host_pid": "9e6742732c60:1",
  "hash": "66fda3ac039d124d72ea19f1e83f2f8ccd964766573c0595c950dcbbaa5cbbd0",
  "cid": "QmV166fda3ac039d124d72ea19f1e83f2f8ccd964766",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286066,
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
      "evaluated_at": 1760286066
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
  "sig": "f33bd54a680e809a67e7b3439b4694cf3498cb51250af94cb87c487f88193b54"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000027745016
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 12, 'first_seen': 1760285765, 'matching_hash': '88a158c93e7cc45f'}}}