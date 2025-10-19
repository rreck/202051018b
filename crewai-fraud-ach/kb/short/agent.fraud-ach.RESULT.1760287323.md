```json
{
  "id": "670874f0604c50d9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287323,
  "host_pid": "9e6742732c60:1",
  "hash": "e0b44d3dcf1bcff2d7b5dae0834bb07027653651c9748baeeca40732269eba45",
  "cid": "QmV1e0b44d3dcf1bcff2d7b5dae0834bb07027653651",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287323,
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
      "evaluated_at": 1760287323
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
  "sig": "4330d5fb2e1268f84b8afb9b129c5fe315b49afb9b6f321d24bea208d903584f"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 021000022625380
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 56, 'threshold': 50, 'total_amount': 20254696, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 55, 'first_seen': 1760285763, 'matching_hash': 'f6638b44b9180b42'}}}