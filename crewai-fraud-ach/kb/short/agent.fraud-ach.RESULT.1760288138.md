```json
{
  "id": "b8f21253a615f6ef",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288138,
  "host_pid": "9e6742732c60:1",
  "hash": "9de9fe78497f76641bec6ae53a897d62cb1fa5c09038b27ad9ba398156a1b42f",
  "cid": "QmV19de9fe78497f76641bec6ae53a897d62cb1fa5c0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288138,
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
      "evaluated_at": 1760288138
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
  "sig": "e28eaf45e8fdc40c6d790bf6328ae73f3b6c291da8ac7b419adaed9357589ab1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000035593386
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 84, 'threshold': 50, 'total_amount': 10025820, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 83, 'first_seen': 1760285763, 'matching_hash': '6253d15ae41563d2'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '987899137', 'validation_error': 'Invalid routing number checksum'}}}