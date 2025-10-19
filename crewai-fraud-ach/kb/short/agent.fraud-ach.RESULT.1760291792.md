```json
{
  "id": "527014d4c73d7720",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291792,
  "host_pid": "9e6742732c60:1",
  "hash": "f232f56f143087d75a7858820a3582f50930c9cab8873655a2e673676a1f81a0",
  "cid": "QmV1f232f56f143087d75a7858820a3582f50930c9ca",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291792,
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
      "evaluated_at": 1760291792
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
  "sig": "3f5a2b1aac9bddd4257741d98581e341f8ca5a660a63aa85bb54d1b665f79cb5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465603072
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 183, 'threshold': 50, 'total_amount': 11070219, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 182, 'first_seen': 1760285763, 'matching_hash': 'e359f7b1cd5a9343'}}}