```json
{
  "id": "8fd495601c5da62c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288768,
  "host_pid": "9e6742732c60:1",
  "hash": "7dd353280ca93def8d76ddad9a95ae62e82f24cc4935856183df0f4f3dc8672b",
  "cid": "QmV17dd353280ca93def8d76ddad9a95ae62e82f24cc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288768,
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
      "evaluated_at": 1760288768
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
  "sig": "ff5f6f1007d14196bf2cae23b1d5fa1b13f3339a2d5d2c31c2e16b8c7b35ce04"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243970709
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 103, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 102, 'first_seen': 1760285765, 'matching_hash': '886d04c9297a738f'}}}