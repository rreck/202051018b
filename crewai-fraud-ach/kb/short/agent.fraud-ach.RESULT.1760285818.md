```json
{
  "id": "801a5b131b4d7241",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285818,
  "host_pid": "9e6742732c60:1",
  "hash": "b7d532cc8fb3d2c37280c90d72b9256b5b2c87b3b24acdd4b28380baccecdf2e",
  "cid": "QmV1b7d532cc8fb3d2c37280c90d72b9256b5b2c87b3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285818,
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
      "evaluated_at": 1760285818
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
  "sig": "9730d37fcac6c9919aabacbb3a5dc55dcf9a92c1e52f35f30e988957e695e5e8"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000241612576
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 3, 'first_seen': 1760285763, 'matching_hash': 'a67f7546b45b9310'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '580123066', 'validation_error': 'Invalid routing number checksum'}}}