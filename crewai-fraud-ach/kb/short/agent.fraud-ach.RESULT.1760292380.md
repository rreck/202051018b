```json
{
  "id": "c58e207e7188fcc0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292380,
  "host_pid": "9e6742732c60:1",
  "hash": "12a40dc59ddf2fc1b9f1e7c39391689d63b6f47c7f44f53e2a6f4bcc5679bce1",
  "cid": "QmV112a40dc59ddf2fc1b9f1e7c39391689d63b6f47c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292380,
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
      "evaluated_at": 1760292380
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
  "sig": "d435999cee0ae4ead73a0a02db35f541f90ad02cf3f2ccdb5048c84ea08d666a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029313979
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 196, 'threshold': 50, 'total_amount': 92634892, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 195, 'first_seen': 1760285765, 'matching_hash': 'ee97e2abac1557d2'}}}