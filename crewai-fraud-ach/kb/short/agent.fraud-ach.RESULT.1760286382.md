```json
{
  "id": "e725a864ce71dc3f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286382,
  "host_pid": "9e6742732c60:1",
  "hash": "3cc61dd5a00ed9eb5a397302745096462842b36a95efa437de26145339997239",
  "cid": "QmV13cc61dd5a00ed9eb5a397302745096462842b36a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286382,
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
      "evaluated_at": 1760286382
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
  "sig": "801e3400e29c3e9d35508d32450701c3dd686f824abdc72039a79204fc05d9b1"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105156608425
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 22, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}