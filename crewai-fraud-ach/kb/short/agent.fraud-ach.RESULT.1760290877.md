```json
{
  "id": "fcbc5fdb631cc57f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290877,
  "host_pid": "9e6742732c60:1",
  "hash": "dd06976d17d65a28a13d186c303ad7ba44b67f54c99f2b9840f373c77d5c6086",
  "cid": "QmV1dd06976d17d65a28a13d186c303ad7ba44b67f54",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290877,
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
      "evaluated_at": 1760290877
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
  "sig": "7bd086bed8894dfa0464a4888d1c2d149f57869f54e5f181de2d479686d3d130"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274571178
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 161, 'threshold': 50, 'total_amount': 76629077, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 160, 'first_seen': 1760285765, 'matching_hash': '2fe0a786c074c752'}}}