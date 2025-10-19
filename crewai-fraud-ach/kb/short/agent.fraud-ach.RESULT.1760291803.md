```json
{
  "id": "9f49fd6e792f624c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291803,
  "host_pid": "9e6742732c60:1",
  "hash": "756d5a6c2e56ade1ceaff29e9f6222a5dc94dc3f57e88492dc9d4aff9797475b",
  "cid": "QmV1756d5a6c2e56ade1ceaff29e9f6222a5dc94dc3f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291803,
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
      "evaluated_at": 1760291803
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
  "sig": "6ac1ac5b9add31655cab719a1cc8dcd45ff90cef7e1cd683cc5b131f90a2ed0b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038917834
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 183, 'threshold': 50, 'total_amount': 53160036, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 182, 'first_seen': 1760285765, 'matching_hash': '760f57350f86dbe3'}}}