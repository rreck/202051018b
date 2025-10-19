```json
{
  "id": "5cf5f4a635ebaa34",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290288,
  "host_pid": "9e6742732c60:1",
  "hash": "1ac292c82eccf3b1cdfb1f67b1808a8ea5e1bcd0d9d8e56caaeae6e6bfc6025c",
  "cid": "QmV11ac292c82eccf3b1cdfb1f67b1808a8ea5e1bcd0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290288,
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
      "evaluated_at": 1760290288
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
  "sig": "a3c0f364a425199e949ca6ea358547ea0f37f1649027e526a1fc2187cab045a6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033751291
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 146, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 145, 'first_seen': 1760285765, 'matching_hash': '04859aaf1143bd8f'}}}