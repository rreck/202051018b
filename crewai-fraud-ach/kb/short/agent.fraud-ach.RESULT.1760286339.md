```json
{
  "id": "880b569a2e880130",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286339,
  "host_pid": "9e6742732c60:1",
  "hash": "d7c3011f8093c3a27b3388e57fba8ba90f9bb68cbd152c909645402624c7c80c",
  "cid": "QmV1d7c3011f8093c3a27b3388e57fba8ba90f9bb68c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286339,
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
      "evaluated_at": 1760286339
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
  "sig": "a90cc00ee7602fda6d996e11c305b6890d7e1f080adbeea472abbe9787546792"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009590178584
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 21, 'first_seen': 1760285763, 'matching_hash': 'edc4255e13a93cc1'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '789209527', 'validation_error': 'Invalid routing number checksum'}}}