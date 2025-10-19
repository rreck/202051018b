```json
{
  "id": "18473485468a5d3b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287330,
  "host_pid": "9e6742732c60:1",
  "hash": "f9cb67ec8042908c1b72597a8266a79f61260406f0d391c0a69e84634f9fce9a",
  "cid": "QmV1f9cb67ec8042908c1b72597a8266a79f61260406",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287330,
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
      "evaluated_at": 1760287330
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "4f79083e2f741886f2e5b1e515df3ad37169bf3a0ba18304f4568c0304fa0f8a"
}
```

Fraud detected: duplicate_transaction (score: 73)
Transaction: 122105151422831
Details: {'velocity': {'fraud_detected': True, 'risk_score': 62, 'details': {'transaction_count': 56, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 55, 'first_seen': 1760285764, 'matching_hash': 'e9fc645b92693d6a'}}}