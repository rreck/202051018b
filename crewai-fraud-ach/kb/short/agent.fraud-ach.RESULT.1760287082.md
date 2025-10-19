```json
{
  "id": "ebcdfe581121e0a2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287082,
  "host_pid": "9e6742732c60:1",
  "hash": "55cf5aaf1c3dcc627db7295fb43c81e6c109201c16136a4aac354b945d2c6a80",
  "cid": "QmV155cf5aaf1c3dcc627db7295fb43c81e6c109201c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287082,
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
      "evaluated_at": 1760287082
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
  "sig": "47cbdeb4dd96327f4f14d775859c964376236f1f5e08c3f5f0f6dfe68754e638"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 14957656, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 46, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}