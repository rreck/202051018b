```json
{
  "id": "0a7e5331816c5ef3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293985,
  "host_pid": "9e6742732c60:1",
  "hash": "b913533fa4511679160476a8496f3e8c106ecb5ff25587c4d66f69c2128fd8ee",
  "cid": "QmV1b913533fa4511679160476a8496f3e8c106ecb5f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293985,
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
      "evaluated_at": 1760293985
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
  "sig": "37f12f906d10c0ba9ed790c398cb6c6e60e528d36a51f68cb0595433e87087e4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026081546
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 35755831, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760285763, 'matching_hash': 'ce75c9757255dcb1'}}}