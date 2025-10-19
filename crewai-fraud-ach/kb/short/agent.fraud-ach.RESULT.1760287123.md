```json
{
  "id": "604a039ab784ca5c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287123,
  "host_pid": "9e6742732c60:1",
  "hash": "0681c29fa811065d4462a8e212ba7c37e6d51a8f63fdc7df231eb9c7db23e173",
  "cid": "QmV10681c29fa811065d4462a8e212ba7c37e6d51a8f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287123,
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
      "evaluated_at": 1760287123
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
  "sig": "9ab05d00d2ead98137d29d00cc4ebe3093d1b93fabe5b46dc95545766293772d"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 372851334846795
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 24103982, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 48, 'first_seen': 1760285763, 'matching_hash': 'e24b6b5408d67f01'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '372851336', 'validation_error': 'Invalid routing number checksum'}}}