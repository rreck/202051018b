```json
{
  "id": "ae9429942d6694e5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288829,
  "host_pid": "9e6742732c60:1",
  "hash": "bdbf41721446d3caf8aa907ad0c58e20fc79af3a99e2181172b8fa8c126780a9",
  "cid": "QmV1bdbf41721446d3caf8aa907ad0c58e20fc79af3a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288829,
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
      "evaluated_at": 1760288829
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
  "sig": "58e68ff97331e2c0dd73a13d9ba1487d24695f771d40005ae301af61d26e4807"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468284841
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 105, 'threshold': 50, 'total_amount': 19666815, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 104, 'first_seen': 1760285764, 'matching_hash': 'af26bab6e9f38d2a'}}}