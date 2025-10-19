```json
{
  "id": "5daf5e781fedc28d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292479,
  "host_pid": "9e6742732c60:1",
  "hash": "7f163a83a31373c80642232631790b706947c26a1a5b4f8ab70fbf4f1ad79708",
  "cid": "QmV17f163a83a31373c80642232631790b706947c26a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292479,
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
      "evaluated_at": 1760292479
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
  "sig": "ca4a7d9b76c77493aa23ec6d4d6f4a04b62b68057e2c831e0b32d75924a39ab9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274578801
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 198, 'threshold': 50, 'total_amount': 34776720, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 197, 'first_seen': 1760285765, 'matching_hash': 'c58645b7bcecdbfd'}}}