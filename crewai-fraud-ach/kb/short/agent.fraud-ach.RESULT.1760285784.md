```json
{
  "id": "e648dc1106f77869",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285784,
  "host_pid": "9e6742732c60:1",
  "hash": "4e94a75de799b3fae0083b0ec663dc1c013b1fc2a363ad09c3adec09562a3bf3",
  "cid": "QmV14e94a75de799b3fae0083b0ec663dc1c013b1fc2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285784,
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
      "evaluated_at": 1760285784
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
  "sig": "39a1671c72c5943f59d25c9840bc93e25950561acec5e390bbd3ca8bd3736c01"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100278681806
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 1, 'first_seen': 1760285765, 'matching_hash': '5ddc61c49d89e409'}}}