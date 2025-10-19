```json
{
  "id": "6c51a51f1d41b75a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286009,
  "host_pid": "9e6742732c60:1",
  "hash": "8f49ea6fafcc4577acfcf957bc3c91d5778d6a6ab04a7b4ff1377576071ac85e",
  "cid": "QmV18f49ea6fafcc4577acfcf957bc3c91d5778d6a6a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286009,
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
      "evaluated_at": 1760286009
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
  "sig": "2ebcbb58df5e146d618ba5ad1cab5844f3b0d14c5655737b955d776663ad8d1f"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000029441717
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 10, 'first_seen': 1760285764, 'matching_hash': 'f6bac04718607b3a'}}}