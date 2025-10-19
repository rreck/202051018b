```json
{
  "id": "b764d209481f11ab",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290397,
  "host_pid": "9e6742732c60:1",
  "hash": "28a2981f1151006f75a23b4b41811e609b24bb11aae44f654f02287f830d2dc3",
  "cid": "QmV128a2981f1151006f75a23b4b41811e609b24bb11",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290397,
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
      "evaluated_at": 1760290397
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
  "sig": "d47e4c53b4582234e673a6eeaa41f74d328d51ef7facde25138b6ddece4c9883"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279970164
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 149, 'threshold': 50, 'total_amount': 27513148, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 148, 'first_seen': 1760285765, 'matching_hash': 'dc8a7598801f2a18'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '288759214', 'validation_error': 'Invalid routing number checksum'}}}