```json
{
  "id": "d6aa9507d074c54f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291502,
  "host_pid": "9e6742732c60:1",
  "hash": "c9faab1126d11494bbb423758106a07f5b077d58fa8d4913b497a72aa03b0551",
  "cid": "QmV1c9faab1126d11494bbb423758106a07f5b077d58",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291502,
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
      "evaluated_at": 1760291502
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
  "sig": "90d148f5cb8f10d4629b4224c932243785f12148be864c871b62d47a0c67d4d9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467876303
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 176, 'threshold': 50, 'total_amount': 77023584, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 175, 'first_seen': 1760285765, 'matching_hash': 'ffdb832f59bf640d'}}}