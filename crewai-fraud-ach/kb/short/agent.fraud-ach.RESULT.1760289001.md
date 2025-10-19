```json
{
  "id": "3138dfc07c6be961",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289001,
  "host_pid": "9e6742732c60:1",
  "hash": "1a7bd16b894abe29f6536430a8c9a032cc67381a151974481f303c000a006efe",
  "cid": "QmV11a7bd16b894abe29f6536430a8c9a032cc67381a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289001,
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
      "evaluated_at": 1760289001
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
  "sig": "09b263e0bc5a142914ba8bf8fced5c23a7c8a36c8dd04bc9be2b45b9fba9d9c0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023496704
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 110, 'threshold': 50, 'total_amount': 37295830, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 109, 'first_seen': 1760285765, 'matching_hash': 'f379baac52e28232'}}}