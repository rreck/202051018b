```json
{
  "id": "69c1f89fc6049a8a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286622,
  "host_pid": "9e6742732c60:1",
  "hash": "c5caddae8b4328ef35a0f1097256982bf70308acfd7038e69aba02bf32052aaa",
  "cid": "QmV1c5caddae8b4328ef35a0f1097256982bf70308ac",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286622,
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
      "evaluated_at": 1760286622
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "a0a4dbea0ea7e5c1b274fadef30d61c191f21d0b8f52cf7a6ec1e43285699dd5"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 021000025329406
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 15014137, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 30, 'first_seen': 1760285765, 'matching_hash': '4bb9b304f38123bb'}}}