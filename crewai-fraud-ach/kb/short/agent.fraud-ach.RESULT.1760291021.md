```json
{
  "id": "037e62d03ae41b90",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291021,
  "host_pid": "9e6742732c60:1",
  "hash": "f5c457f7c64ff6e7ec89cab4c6e280f87b669db7d43f800de418753eec4f6096",
  "cid": "QmV1f5c457f7c64ff6e7ec89cab4c6e280f87b669db7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291021,
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
      "evaluated_at": 1760291021
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
  "sig": "cfdb60798d1f0a101439c5cffc71641e64a0a9374d6f8342381eec8e0deed02e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598799064
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 165, 'threshold': 50, 'total_amount': 62084880, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 164, 'first_seen': 1760285763, 'matching_hash': '14e8b5e643b0ea13'}}}