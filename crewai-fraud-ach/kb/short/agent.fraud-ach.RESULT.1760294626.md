```json
{
  "id": "6237a06804b8715e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294626,
  "host_pid": "9e6742732c60:1",
  "hash": "5e07b154550a8722beb521af1d8c4849e31905a34bb9e208fcf82c576f71e784",
  "cid": "QmV15e07b154550a8722beb521af1d8c4849e31905a3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294626,
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
      "evaluated_at": 1760294626
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
  "sig": "155ac437240c9be535e3b6259db59a0d83a9b3792705da4826c86ae99e1077b8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274578801
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 42329240, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285765, 'matching_hash': 'c58645b7bcecdbfd'}}}