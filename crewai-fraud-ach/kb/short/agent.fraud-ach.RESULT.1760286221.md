```json
{
  "id": "2c6cd32164982d2c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286221,
  "host_pid": "9e6742732c60:1",
  "hash": "4f72ec0523695d4620f16ec9ca8e244da062c96ce5eec2b2ca888d4cac9704d4",
  "cid": "QmV14f72ec0523695d4620f16ec9ca8e244da062c96c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286221,
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
      "evaluated_at": 1760286221
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
  "sig": "afdc8f830b8ece6d887b5e9b65d740673208d9ff1b34363b4a0b7429cad290b2"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000039498282
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 17, 'first_seen': 1760285765, 'matching_hash': 'dad018b424b66512'}}}