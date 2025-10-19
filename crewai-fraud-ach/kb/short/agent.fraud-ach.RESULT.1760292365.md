```json
{
  "id": "f36269cb1db55494",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292365,
  "host_pid": "9e6742732c60:1",
  "hash": "c5cbea929d72f15a6916bb22f031468c509555ce5107a6c1a863a37a9dd96425",
  "cid": "QmV1c5cbea929d72f15a6916bb22f031468c509555ce",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292365,
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
      "evaluated_at": 1760292365
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
  "sig": "db7b9e35c8d6556c4a4557a3a9987eb1f54bcf436c0c30880b364f2de686421c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242260871
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 196, 'threshold': 50, 'total_amount': 65237816, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 195, 'first_seen': 1760285764, 'matching_hash': '677d45847b06d7dd'}}}