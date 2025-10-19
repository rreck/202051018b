```json
{
  "id": "05a1a833aeb381f9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293558,
  "host_pid": "9e6742732c60:1",
  "hash": "63eb9f79545a07ad12fa6970cc303eb91a217d389e00ec4844b19da66ba5ebce",
  "cid": "QmV163eb9f79545a07ad12fa6970cc303eb91a217d38",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293558,
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
      "evaluated_at": 1760293558
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
  "sig": "924c39ddaa6cfe281fd955ebecd2f2e48784545182050af0a685ecc2ad22a0f7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037838000
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 25832469, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285763, 'matching_hash': 'ae4ad01d54e54763'}}}