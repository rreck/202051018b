```json
{
  "id": "26d5e677850d70d8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286217,
  "host_pid": "9e6742732c60:1",
  "hash": "39326c0a728a7bf7fa07b8ea312f516641c26f0c6f0b2b556a2329723b7f64c7",
  "cid": "QmV139326c0a728a7bf7fa07b8ea312f516641c26f0c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286217,
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
      "evaluated_at": 1760286217
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
  "sig": "39490d9507dafc902dd353604878e97ca7e10aff8eb02153e4d292f6cb7ed168"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000245329334
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 17, 'first_seen': 1760285765, 'matching_hash': 'de3fbc58a94e529a'}}}