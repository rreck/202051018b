```json
{
  "id": "1611820051b06e24",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294499,
  "host_pid": "9e6742732c60:1",
  "hash": "30b9f32566790ea9570a81aa6c0970d9cb076a891ec7d0141bc9e923c3f42440",
  "cid": "QmV130b9f32566790ea9570a81aa6c0970d9cb076a89",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294499,
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
      "evaluated_at": 1760294499
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
  "sig": "b5d4019bbd1058a9deadf54b5fd6a1415babe7a9faaa989949cc2254226d6e7d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157192911
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 64156921, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285764, 'matching_hash': 'e4f1eedb707bab1f'}}}