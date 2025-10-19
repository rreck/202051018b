```json
{
  "id": "23cb01375ae524b5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294547,
  "host_pid": "9e6742732c60:1",
  "hash": "caffb3ac1524553e5d31c626780ab3331ac9a3657bb8829712abd6c677826fd4",
  "cid": "QmV1caffb3ac1524553e5d31c626780ab3331ac9a365",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294547,
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
      "evaluated_at": 1760294547
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
  "sig": "538d94d7aa8211133eb3f00a8cbd42d53af9dc782e38c4c00e43be4181601fb9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469437118
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 55633920, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285763, 'matching_hash': '2ba59ce16e89c25c'}}}}