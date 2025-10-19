```json
{
  "id": "5db5f6476464a661",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290281,
  "host_pid": "9e6742732c60:1",
  "hash": "cbf46bb6fe8c159f8fd31b8bc90d7c745aada32ee322c71cac2765d0c930b0bb",
  "cid": "QmV1cbf46bb6fe8c159f8fd31b8bc90d7c745aada32e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290281,
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
      "evaluated_at": 1760290281
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
  "sig": "39dfa6e0bd3b2a98680aac65b31437c2366acab78eeb48a38e1a90a68944ec91"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100273334011
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 146, 'threshold': 50, 'total_amount': 15169984, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 145, 'first_seen': 1760285763, 'matching_hash': 'fc8e9fbdacff3816'}}}