```json
{
  "id": "8c0795c36c8a4a57",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286380,
  "host_pid": "9e6742732c60:1",
  "hash": "f6fa0b436703460a62c934b17b5102d096c2528702736f97ce19de5d09e456b1",
  "cid": "QmV1f6fa0b436703460a62c934b17b5102d096c25287",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286380,
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
      "evaluated_at": 1760286380
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
  "sig": "adb6a07cc661ccfeaa8255a51f2ae1354aa2efc1abfb2705d082bf06598a44e8"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201460708628
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 22, 'first_seen': 1760285765, 'matching_hash': 'f97c6efa7b54b0cd'}}}