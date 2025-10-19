```json
{
  "id": "82958d5b41ea707b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290006,
  "host_pid": "9e6742732c60:1",
  "hash": "79db44ef3604c062a0a2b69966a17d488276cf1d7ddc22f40f11f760a49bb3a4",
  "cid": "QmV179db44ef3604c062a0a2b69966a17d488276cf1d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290006,
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
      "evaluated_at": 1760290006
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
  "sig": "df22b9e66e30db2e65651406c38f2b418bbabfbe7a37b57774559af746d983cc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000036907843
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 139, 'threshold': 50, 'total_amount': 42847028, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 138, 'first_seen': 1760285763, 'matching_hash': '5c57e03938e1b0ed'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '646437635', 'validation_error': 'Invalid routing number checksum'}}}