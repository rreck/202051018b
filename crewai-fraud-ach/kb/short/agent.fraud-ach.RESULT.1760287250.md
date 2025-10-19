```json
{
  "id": "f24805c47a4edf4d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287250,
  "host_pid": "9e6742732c60:1",
  "hash": "316b84ee8f7624385f45d70c4ccd823d12657bce302c940971ede6f025f655d7",
  "cid": "QmV1316b84ee8f7624385f45d70c4ccd823d12657bce",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287250,
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
      "evaluated_at": 1760287250
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
  "sig": "b86a64a40b31a9a2a2966e2ab79139f365c9713c2f0429dbcc80b800ae652a6b"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 021000021513577
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 53, 'threshold': 50, 'total_amount': 12082675, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 52, 'first_seen': 1760285765, 'matching_hash': '2d9e7d16ad0b5ba4'}}}