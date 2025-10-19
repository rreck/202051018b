```json
{
  "id": "8a75c6f0ccdb1c3a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288366,
  "host_pid": "9e6742732c60:1",
  "hash": "7b60dfa7a0f593742f8d1cc040bf7ba018aa1c5417b55eec4fae93bf7b55ed7a",
  "cid": "QmV17b60dfa7a0f593742f8d1cc040bf7ba018aa1c54",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288366,
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
      "evaluated_at": 1760288366
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
  "sig": "2e635c5c950f6fa529ef38ed23b6f4006fabaa73ae09705f9bbe4cafd739faf5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152187504
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 91, 'threshold': 50, 'total_amount': 42992404, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 90, 'first_seen': 1760285764, 'matching_hash': '4c6bc703d31ba532'}}}