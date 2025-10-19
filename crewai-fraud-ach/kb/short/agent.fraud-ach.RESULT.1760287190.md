```json
{
  "id": "f222284b4371b543",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287190,
  "host_pid": "9e6742732c60:1",
  "hash": "6f12c07e163684a01330097b1ee149938984e3b8b13f1ded48293db96dc41178",
  "cid": "QmV16f12c07e163684a01330097b1ee149938984e3b8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287190,
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
      "evaluated_at": 1760287190
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
  "sig": "48d485d413c05cf3ed24bcbfcb139160350f048741496cd13caf58206db878ec"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 021000025001245
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 51, 'threshold': 50, 'total_amount': 10891203, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 50, 'first_seen': 1760285764, 'matching_hash': 'bf601f225a65579b'}}}