```json
{
  "id": "4ee68d6e6982fcad",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286488,
  "host_pid": "9e6742732c60:1",
  "hash": "e2fbefa8d5cee2481585ef2b93c103d835bb4181b8d19147ea480ff21bd5ada8",
  "cid": "QmV1e2fbefa8d5cee2481585ef2b93c103d835bb4181",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286488,
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
      "evaluated_at": 1760286488
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
  "sig": "ee6c22b37fca80765ff5e04756474e01937a754d2ec6c59290c21f0a2ceb9d0b"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009598219972
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 13202001, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 26, 'first_seen': 1760285763, 'matching_hash': '09b5d296b49f9602'}}}