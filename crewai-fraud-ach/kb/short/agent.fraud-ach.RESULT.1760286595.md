```json
{
  "id": "19aacdce1ecb7d6b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286595,
  "host_pid": "9e6742732c60:1",
  "hash": "f8062cd0fa2ee64958ca25287fd88c738f23feda4f45d69f7c1131abdf9c0a15",
  "cid": "QmV1f8062cd0fa2ee64958ca25287fd88c738f23feda",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286595,
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
      "evaluated_at": 1760286595
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
  "sig": "dc600e67fc632eb5ce5945413e9c676270fea3b3457b3406309ec21499b3d262"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105156608425
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 29, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}