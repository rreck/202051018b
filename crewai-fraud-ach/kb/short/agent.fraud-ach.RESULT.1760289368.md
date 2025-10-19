```json
{
  "id": "a580d30c68663a72",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289368,
  "host_pid": "9e6742732c60:1",
  "hash": "afade4e40fa3ca5b3827236b3fe8dd4c724acf6599adedd929dcbb2a14615187",
  "cid": "QmV1afade4e40fa3ca5b3827236b3fe8dd4c724acf65",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289368,
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
      "evaluated_at": 1760289368
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
  "sig": "9eda8914d68a58cc064b6b9d64013e99233fd8a771bfd6b155b2525d8789825e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240116635
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 121, 'threshold': 50, 'total_amount': 45957373, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 120, 'first_seen': 1760285763, 'matching_hash': 'faa8e9f78afe3726'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '789209527', 'validation_error': 'Invalid routing number checksum'}}}