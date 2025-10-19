```json
{
  "id": "59fae436c9b8f55c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292782,
  "host_pid": "9e6742732c60:1",
  "hash": "48236a33c14bb62db58e677a55baf6ccbdedb8737b6f4e68c60a4c3f1ee33d19",
  "cid": "QmV148236a33c14bb62db58e677a55baf6ccbdedb873",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292782,
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
      "evaluated_at": 1760292782
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
  "sig": "2ae52098fa60d1ade5adbf018fbee55ab5b26dc3005f8b401dc6d598ca6ee8f0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100277276019
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 205, 'threshold': 50, 'total_amount': 77485695, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 204, 'first_seen': 1760285763, 'matching_hash': '90b38bd8812494f9'}}}