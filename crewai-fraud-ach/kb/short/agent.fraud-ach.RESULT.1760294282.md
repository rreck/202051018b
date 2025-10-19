```json
{
  "id": "fec05b2e889e8c88",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294282,
  "host_pid": "9e6742732c60:1",
  "hash": "a608e33daf08e92ff980131e134e09f5f4d5b9d24a5e77a5de6cf1283304fc71",
  "cid": "QmV1a608e33daf08e92ff980131e134e09f5f4d5b9d2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294282,
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
      "evaluated_at": 1760294282
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
  "sig": "33c945f75fc979f945ddd3d0f070a5991b6f7def0bf80acaaa8faf554c8cc542"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279304140
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 235, 'threshold': 50, 'total_amount': 30769725, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 234, 'first_seen': 1760285764, 'matching_hash': '56d1c75d448f4ea1'}}}