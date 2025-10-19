```json
{
  "id": "ad0e514a3d7073b8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286902,
  "host_pid": "9e6742732c60:1",
  "hash": "8a100d71e86a2186237b0ce62f9ac5615c87842f69c22247bade4f6687a917e8",
  "cid": "QmV18a100d71e86a2186237b0ce62f9ac5615c87842f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286902,
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
      "evaluated_at": 1760286902
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
  "sig": "22d108276252d5980fb500bbbb0dc2ddd05d507afce3ce2e4f0c09ebe1190fd4"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009593439334
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 15619483, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 40, 'first_seen': 1760285763, 'matching_hash': 'a46c33998c9a26e1'}}}