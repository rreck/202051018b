```json
{
  "id": "7db7ed1ebf2217e0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294139,
  "host_pid": "9e6742732c60:1",
  "hash": "15cbcd442d17b1233c7b7635441a5486406e61c8f895b7659379610d430870b4",
  "cid": "QmV115cbcd442d17b1233c7b7635441a5486406e61c8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294139,
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
      "evaluated_at": 1760294139
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
  "sig": "4fa230185ecec3eba092e5dfb2fa4294b4fcd0f92bd44fcd169e8ae30a50d66e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461436182
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 31249008, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285765, 'matching_hash': 'd641045bf224534b'}}}