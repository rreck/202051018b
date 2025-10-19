```json
{
  "id": "35f4ea71a1e3abcc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289896,
  "host_pid": "9e6742732c60:1",
  "hash": "940e8145bd9f2b42592fe250fd60eec6d975a7173d7d38f91239a0f0a997d7b5",
  "cid": "QmV1940e8145bd9f2b42592fe250fd60eec6d975a717",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289896,
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
      "evaluated_at": 1760289896
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
  "sig": "3415583979d8a8ed767296325c980933c52e9a7e7e8cb1d961b627e3592a457c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465723283
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 136, 'threshold': 50, 'total_amount': 58145304, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 135, 'first_seen': 1760285764, 'matching_hash': 'e1350af409930159'}}}