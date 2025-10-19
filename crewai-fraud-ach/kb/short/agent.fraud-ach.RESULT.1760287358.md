```json
{
  "id": "5c991fb53afb87e0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287358,
  "host_pid": "9e6742732c60:1",
  "hash": "dd7cd7bf3aef76ef6006360a44013a24b02de5c37e3172b028765ed2ee93287a",
  "cid": "QmV1dd7cd7bf3aef76ef6006360a44013a24b02de5c3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287358,
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
      "evaluated_at": 1760287358
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
  "sig": "9f5cb60e661788f3dd5745d41d7cf0f2f54a528d159ffd5614b78bb2b386f102"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201462505262
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 57, 'threshold': 50, 'total_amount': 22317438, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 56, 'first_seen': 1760285764, 'matching_hash': 'e15f6eb56271d036'}}}