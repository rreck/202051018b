```json
{
  "id": "fa1704a7aa8f09f6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286029,
  "host_pid": "9e6742732c60:1",
  "hash": "3e83ba1d928fb0eab05f62da82a65123c8dea7ea5ca43ee0775ecb437cebaf2b",
  "cid": "QmV13e83ba1d928fb0eab05f62da82a65123c8dea7ea",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286029,
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
      "evaluated_at": 1760286029
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
  "sig": "8c39d200397459a24e72bc2159721fe8aa94985cbd661f37adf3599e30a40e23"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201462917660
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 11, 'first_seen': 1760285763, 'matching_hash': '3c31ab634de6a3e3'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '472304300', 'validation_error': 'Invalid routing number checksum'}}}