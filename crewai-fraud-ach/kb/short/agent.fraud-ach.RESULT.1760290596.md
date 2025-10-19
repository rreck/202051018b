```json
{
  "id": "09ddc4804aff6d70",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290596,
  "host_pid": "9e6742732c60:1",
  "hash": "9018a81b544839ecccb88beab77e84188fdda4dbc7e44ab025282915bcbc7b82",
  "cid": "QmV19018a81b544839ecccb88beab77e84188fdda4db",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290596,
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
      "evaluated_at": 1760290596
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "46fe3644825c4a24a320319f6cdc79eda99de92c9ed12de762aa961e2c4ef922"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 109883193945676
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 154, 'threshold': 50, 'total_amount': 46370940, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 153, 'first_seen': 1760285765, 'matching_hash': '153e74d04ee716fe'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '109883192', 'validation_error': 'Invalid routing number checksum'}}}