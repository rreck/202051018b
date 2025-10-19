```json
{
  "id": "67c8e924cccd9243",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290242,
  "host_pid": "9e6742732c60:1",
  "hash": "241805af31f978e389d7c81fc9f58977297437a3b5d93317e55914d765421d76",
  "cid": "QmV1241805af31f978e389d7c81fc9f58977297437a3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290242,
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
      "evaluated_at": 1760290242
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
  "sig": "ce6fd2fddbee65e7a56a8e50f62f7b283221f39766d8d1adc65daf55bfbcba7c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245537248
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 145, 'threshold': 50, 'total_amount': 21198275, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 144, 'first_seen': 1760285765, 'matching_hash': '5bdcebee79eae34d'}}}