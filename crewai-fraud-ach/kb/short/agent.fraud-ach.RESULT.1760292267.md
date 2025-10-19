```json
{
  "id": "668835264019f930",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292267,
  "host_pid": "9e6742732c60:1",
  "hash": "63d6fc9cdb29cf82a15785358fe91a89e6ca5ddb18b81fc6f3566a297ba3f371",
  "cid": "QmV163d6fc9cdb29cf82a15785358fe91a89e6ca5ddb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292267,
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
      "evaluated_at": 1760292267
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
  "sig": "1e9f4ec3a9dede06067cc1d0b2bc694642625b176b2d3fa1913b2765a1daf4c8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462461467
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 194, 'threshold': 50, 'total_amount': 71721994, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 193, 'first_seen': 1760285763, 'matching_hash': '257546013422e30a'}}}