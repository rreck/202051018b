```json
{
  "id": "0935ade280393a12",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285819,
  "host_pid": "9e6742732c60:1",
  "hash": "18bdfb7c5836167db8ddf05490c43131efc5cde0fc1ff1636c1d545e33eca4b2",
  "cid": "QmV118bdfb7c5836167db8ddf05490c43131efc5cde0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285819,
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
      "evaluated_at": 1760285819
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
  "sig": "e5e4decd1e26fb9d6778afeaf6665207fef1f67a458cccb8e267f2e2942216cc"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000028831887
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 3, 'first_seen': 1760285763, 'matching_hash': '597950b73179eb3f'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '398958456', 'validation_error': 'Invalid routing number checksum'}}}