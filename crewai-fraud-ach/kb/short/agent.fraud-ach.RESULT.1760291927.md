```json
{
  "id": "22bb7110cd897219",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291927,
  "host_pid": "9e6742732c60:1",
  "hash": "b493c9f5966f38238f1f1c9c08fca051dea6b497017e73e98e0016a408894af8",
  "cid": "QmV1b493c9f5966f38238f1f1c9c08fca051dea6b497",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291927,
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
      "evaluated_at": 1760291927
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
  "sig": "3caaa72f95254a0f105820a546d85c781517a1c9069dd18bd6f8a767ae36f279"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009595235556
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 186, 'threshold': 50, 'total_amount': 32469276, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 185, 'first_seen': 1760285765, 'matching_hash': 'e45b9dbcffb11ba0'}}}