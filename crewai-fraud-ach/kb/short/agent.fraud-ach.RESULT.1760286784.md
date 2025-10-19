```json
{
  "id": "ef20b0ac066ba28e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286784,
  "host_pid": "9e6742732c60:1",
  "hash": "e4ad7f5e2579c739b7ed8db157ad37d4af7676e1165e1f5ff8f61dbf7af88ee0",
  "cid": "QmV1e4ad7f5e2579c739b7ed8db157ad37d4af7676e1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286784,
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
      "evaluated_at": 1760286784
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "66a347cc8cb0de93280a0d2c7e2ba2424dba3ee86b3ca7278d4a724adf71bb95"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105152772165
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10752422, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 36, 'first_seen': 1760285764, 'matching_hash': '9371db7725d4e0a9'}}}