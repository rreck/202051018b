```json
{
  "id": "235822da2f300353",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289440,
  "host_pid": "9e6742732c60:1",
  "hash": "38e823e28d42199cadddebc507ce414794ddf64f995a6196640d63c0a764f9f7",
  "cid": "QmV138e823e28d42199cadddebc507ce414794ddf64f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289440,
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
      "evaluated_at": 1760289440
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
  "sig": "8f867917e8cb9cd01df2073f626c4022658ca9ff95c6961238b376a05322495f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462554282
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 123, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 122, 'first_seen': 1760285763, 'matching_hash': '2083692f538c0312'}}}