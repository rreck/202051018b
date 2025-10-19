```json
{
  "id": "d18b7b59c80146e1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286209,
  "host_pid": "9e6742732c60:1",
  "hash": "bfc974c62ed6f682045c1b32b612f46069723d5aded5506b9d0c8dd86d7f1e19",
  "cid": "QmV1bfc974c62ed6f682045c1b32b612f46069723d5a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286209,
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
      "evaluated_at": 1760286209
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
  "sig": "dfc5d33683ed0ca1b32aac364f4f0bf37dcd1eec553913b4d4e419f313875721"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009597385398
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 17, 'first_seen': 1760285763, 'matching_hash': '354842811986f77e'}}}