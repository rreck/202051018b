```json
{
  "id": "d7f28111ebe4a40b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292831,
  "host_pid": "9e6742732c60:1",
  "hash": "0c440a924f1b25db5815f1f86d40eb21a097573c3c200b0c7ace458e01c9fbe6",
  "cid": "QmV10c440a924f1b25db5815f1f86d40eb21a097573c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292831,
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
      "evaluated_at": 1760292831
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
  "sig": "74c4f0ce0d9bd13967fac5267a54208f3795fbf8084ff918fd0ac5db5ca82e5a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028116675
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 206, 'threshold': 50, 'total_amount': 70121370, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 205, 'first_seen': 1760285763, 'matching_hash': '276303153292771e'}}}