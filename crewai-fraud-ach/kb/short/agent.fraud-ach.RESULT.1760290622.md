```json
{
  "id": "3afc38845ae25124",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290622,
  "host_pid": "9e6742732c60:1",
  "hash": "b1f281669fa63d0f84f01803fa5676363fca7911d0dfd3ed7592cb009137dffb",
  "cid": "QmV1b1f281669fa63d0f84f01803fa5676363fca7911",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290622,
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
      "evaluated_at": 1760290622
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
  "sig": "191d6d1e0802f75e34d30e4bc5dc8c03fbd5decb983e5f2e032cbe1bcdeaff13"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100277234112
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 155, 'threshold': 50, 'total_amount': 58436240, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 154, 'first_seen': 1760285765, 'matching_hash': '11106d4d9e5d055e'}}}