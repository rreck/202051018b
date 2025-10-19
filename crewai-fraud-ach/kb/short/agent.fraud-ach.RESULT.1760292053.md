```json
{
  "id": "f863f285b3f5aaf4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292053,
  "host_pid": "9e6742732c60:1",
  "hash": "63381a6b69f7072f186c21e0f22a874090208d8c89bf49cf2041bbeae9307a69",
  "cid": "QmV163381a6b69f7072f186c21e0f22a874090208d8c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292053,
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
      "evaluated_at": 1760292053
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
  "sig": "9e7af8cbdd2caad6a1158f99ad07863dd40fef3b30002aae761d56c76f39a5c4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034056272
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 189, 'threshold': 50, 'total_amount': 26123958, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 188, 'first_seen': 1760285763, 'matching_hash': 'aae4e2a94575911d'}}}