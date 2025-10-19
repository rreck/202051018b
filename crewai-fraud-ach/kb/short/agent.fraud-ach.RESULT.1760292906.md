```json
{
  "id": "b5454553f563c025",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292906,
  "host_pid": "9e6742732c60:1",
  "hash": "75570c9d41920d1f98ce5c30730a5f71fc0d35e819876462f13f3cdb14deacd1",
  "cid": "QmV175570c9d41920d1f98ce5c30730a5f71fc0d35e8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292906,
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
      "evaluated_at": 1760292906
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
  "sig": "a433906b0949862ee50263a1f8833eb98564a3a0f17de0fa0e54b1addf788437"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461662832
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 207, 'threshold': 50, 'total_amount': 86511924, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 206, 'first_seen': 1760285765, 'matching_hash': 'adb809538e6eb6af'}}}