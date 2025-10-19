```json
{
  "id": "935c71976b922bfa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289621,
  "host_pid": "9e6742732c60:1",
  "hash": "0017173951066af052d300b690d6fcc4f31984c834050a2655d9280ff5c65e0b",
  "cid": "QmV10017173951066af052d300b690d6fcc4f31984c8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289621,
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
      "evaluated_at": 1760289621
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
  "sig": "2f7dad527ea798d1f5b21946069a387e8bd5c9166c16ddb2f16203f919101910"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000024109289
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 128, 'threshold': 50, 'total_amount': 44719232, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 127, 'first_seen': 1760285765, 'matching_hash': 'ac2c8f9ff893d8ff'}}}