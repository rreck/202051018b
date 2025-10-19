```json
{
  "id": "5a9ee70bd8063940",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290618,
  "host_pid": "9e6742732c60:1",
  "hash": "d0d56b09cc3e346593b6f838e7fa3271c00bec3a2e937ad0e5430084031b5c79",
  "cid": "QmV1d0d56b09cc3e346593b6f838e7fa3271c00bec3a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290618,
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
      "evaluated_at": 1760290618
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
  "sig": "0bde2921b98e1c5ecc1be228a8e41e6843d39077eb3740bb3fa3b8eed250ae5b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247026993
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 155, 'threshold': 50, 'total_amount': 68236115, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 154, 'first_seen': 1760285764, 'matching_hash': '7c7d13001f766fd7'}}}