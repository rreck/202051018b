```json
{
  "id": "6f9d722d9ebbd5b3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286412,
  "host_pid": "9e6742732c60:1",
  "hash": "d37016057fb47f7668bc173930bb95ee4df239df340dedef733713e327ae7f3f",
  "cid": "QmV1d37016057fb47f7668bc173930bb95ee4df239df",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286412,
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
      "evaluated_at": 1760286412
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
  "sig": "999925adefefbe1721a9e862c304a42acb2ad1f8005c668d4fb3ff23ba52416f"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000021933242
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 23, 'first_seen': 1760285765, 'matching_hash': '22fbbd19d3df08b1'}}}