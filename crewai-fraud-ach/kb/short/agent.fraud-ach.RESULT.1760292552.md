```json
{
  "id": "b346838dfa0b9892",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292552,
  "host_pid": "9e6742732c60:1",
  "hash": "e3d1ec239888f85c1560f8ba247e55097de9e0f1da6d1154a41452c7bc07fa08",
  "cid": "QmV1e3d1ec239888f85c1560f8ba247e55097de9e0f1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292552,
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
      "evaluated_at": 1760292552
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
  "sig": "1392ccec9c0bdee79128a456be5f3b1960282699b51f8d7265026012ad62ca18"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028384993
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 200, 'threshold': 50, 'total_amount': 73094600, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 199, 'first_seen': 1760285764, 'matching_hash': '07aae5a269425bd8'}}}