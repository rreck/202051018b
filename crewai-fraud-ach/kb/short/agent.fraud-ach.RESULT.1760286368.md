```json
{
  "id": "7d5b78b01500bceb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286368,
  "host_pid": "9e6742732c60:1",
  "hash": "db82ff086edc7ff9eaab60ffc8e960ece0a0d03d815f105d8bda59def8895e9c",
  "cid": "QmV1db82ff086edc7ff9eaab60ffc8e960ece0a0d03d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286368,
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
      "evaluated_at": 1760286368
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
  "sig": "ed796eedebed496eff00e30bcf0c1ea8397c39e99fe8649e7ab1ea2ca89b7f1c"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201462495850
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 22, 'first_seen': 1760285763, 'matching_hash': '1976ee1fa1c7bc70'}}} 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 98, 'first_seen': 1760284979, 'matching_hash': '7b94effc1b7c4489'}}}