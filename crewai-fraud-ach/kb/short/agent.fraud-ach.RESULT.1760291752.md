```json
{
  "id": "93982aa3a7a6b668",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291752,
  "host_pid": "9e6742732c60:1",
  "hash": "3263d1ac5466de00477b69d17211b9464413b0f21567c4918793c205961e11ab",
  "cid": "QmV13263d1ac5466de00477b69d17211b9464413b0f2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291752,
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
      "evaluated_at": 1760291752
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
  "sig": "099714e2f410589fc0f368cc3b51d0c6c213d242c8e96449af3acbedd89d2296"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009595235556
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 182, 'threshold': 50, 'total_amount': 31771012, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 181, 'first_seen': 1760285765, 'matching_hash': 'e45b9dbcffb11ba0'}}}