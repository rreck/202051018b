```json
{
  "id": "7844a59bdb3895f6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286494,
  "host_pid": "9e6742732c60:1",
  "hash": "c9c912932f8c8ccf23ae8b48fb81a036d2e1ed087c5e2f5d16dcde9f674a5db6",
  "cid": "QmV1c9c912932f8c8ccf23ae8b48fb81a036d2e1ed08",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286494,
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
      "evaluated_at": 1760286494
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
  "sig": "96e32c52d3f16559f36755a0ce6e8eb61f9fce0bc5ead243481704786e06aedf"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000249454336
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 26, 'first_seen': 1760285763, 'matching_hash': '6b4cd9d1923f5d4e'}}}