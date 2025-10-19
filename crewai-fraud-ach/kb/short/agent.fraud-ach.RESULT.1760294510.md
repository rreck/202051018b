```json
{
  "id": "063eaa2b1ef3f87b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294510,
  "host_pid": "9e6742732c60:1",
  "hash": "6fa7ad2183b03fffac98c923aeef6de50cc00a2edc26a25c8b5e2253b0e4ed05",
  "cid": "QmV16fa7ad2183b03fffac98c923aeef6de50cc00a2e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294510,
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
      "evaluated_at": 1760294510
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
  "sig": "e04690b7066658251cbd315fec0d4ec81f992e36dd49153196274089b09e89b0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468256911
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 43383758, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285765, 'matching_hash': 'b0ec3a54cf0504a9'}}} {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '288759214', 'validation_error': 'Invalid routing number checksum'}}}