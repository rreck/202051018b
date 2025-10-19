```json
{
  "id": "dcfc3efeebc950e5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291580,
  "host_pid": "9e6742732c60:1",
  "hash": "d10257e7bc5db4d1f5ab161183b95f4af8f34194fea8db4d4108e330f20ba941",
  "cid": "QmV1d10257e7bc5db4d1f5ab161183b95f4af8f34194",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291580,
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
      "evaluated_at": 1760291580
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
  "sig": "0e5c4ae38645c98208ff3ae8aec5af7a97b22f86f7514b12bb0c9bb2a49c6b77"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460464182
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 178, 'threshold': 50, 'total_amount': 18801962, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 177, 'first_seen': 1760285765, 'matching_hash': '97f231b14306ced8'}}}