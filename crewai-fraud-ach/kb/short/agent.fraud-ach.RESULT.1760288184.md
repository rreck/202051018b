```json
{
  "id": "b2a21f6bafcee00b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288184,
  "host_pid": "9e6742732c60:1",
  "hash": "bb29e1f679d470546d5a79e2778d8fac59d8295b4c146761f5eee1761645042a",
  "cid": "QmV1bb29e1f679d470546d5a79e2778d8fac59d8295b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288184,
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
      "evaluated_at": 1760288184
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
  "sig": "fb30db412825ee1cf6aa494c10ed02da6a3c751a6d4ae2a649d973b48cab8d72"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272414433
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 85, 'threshold': 50, 'total_amount': 12736315, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 84, 'first_seen': 1760285764, 'matching_hash': 'f489e4bd64364941'}}}