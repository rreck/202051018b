```json
{
  "id": "3d157817a436e6ed",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285452,
  "host_pid": "9e6742732c60:1",
  "hash": "a7ce0d3e7c81b63100d691ce406787e2ac044ece2b0800d75aeaa9cf51e8a558",
  "cid": "QmV1a7ce0d3e7c81b63100d691ce406787e2ac044ece",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285452,
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
      "evaluated_at": 1760285452
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "3840bc4511e60c50a41181cc61cc425be26c7d28219da673bcb4dd8f4e0e420e"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 19805518, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 46, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}