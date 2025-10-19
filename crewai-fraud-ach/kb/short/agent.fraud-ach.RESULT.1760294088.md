```json
{
  "id": "7914ee6f0fc42673",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294088,
  "host_pid": "9e6742732c60:1",
  "hash": "ab49f82876da77bc5345d5a5efc2bf102d587c0f9517d9c4de5b19a01378a9ae",
  "cid": "QmV1ab49f82876da77bc5345d5a5efc2bf102d587c0f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294088,
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
      "evaluated_at": 1760294088
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
  "sig": "81e4acbf40648a862225c5c275de918bbeee57211afce94acbd38d645134a8cc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243177921
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 79618770, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285765, 'matching_hash': '2e3fb8f97f4f3efd'}}}