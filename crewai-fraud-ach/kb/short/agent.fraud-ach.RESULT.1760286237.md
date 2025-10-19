```json
{
  "id": "2cbb1edd21ae23f7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286237,
  "host_pid": "9e6742732c60:1",
  "hash": "978f200a0db2102e332068994e7b741a82700b052a12e0e661d74be63ffdeaff",
  "cid": "QmV1978f200a0db2102e332068994e7b741a82700b05",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286237,
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
      "evaluated_at": 1760286237
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
  "sig": "1d332733475f2f5b423e1f3bf661a10298e966f68b1ad3cfc477244f799e9441"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100278201542
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 18, 'first_seen': 1760285763, 'matching_hash': 'ee525b8c336c7bb1'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '701651308', 'validation_error': 'Invalid routing number checksum'}}}