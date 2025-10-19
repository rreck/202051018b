```json
{
  "id": "25b3bea9fa2a9c8f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288657,
  "host_pid": "9e6742732c60:1",
  "hash": "9077280872f8b63763d9c213faf55a73e7a7d80a7b08e4c35a811623edfa673a",
  "cid": "QmV19077280872f8b63763d9c213faf55a73e7a7d80a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288657,
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
      "evaluated_at": 1760288657
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
  "sig": "40a60fc352ba7cbd8d71bf99e1cbf761814ffa0072ddebdca3cac40ea1ca67be"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 886156735269080
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 100, 'threshold': 50, 'total_amount': 19180100, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 99, 'first_seen': 1760285765, 'matching_hash': 'bf20bb751245cb05'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '886156735', 'validation_error': 'Invalid routing number checksum'}}}