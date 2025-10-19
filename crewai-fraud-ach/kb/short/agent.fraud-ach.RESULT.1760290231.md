```json
{
  "id": "2e49c783c37db485",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290231,
  "host_pid": "9e6742732c60:1",
  "hash": "f14c9bcf2394c905a49ef5bf18d9ef43667596508d5c4cd27add5fdc10e88e59",
  "cid": "QmV1f14c9bcf2394c905a49ef5bf18d9ef4366759650",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290231,
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
      "evaluated_at": 1760290231
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
  "sig": "6aa453862d22086cd7fd223af27f6d911f6c5b44551845c8eb99f8a5c9c3af28"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240775358
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 145, 'threshold': 50, 'total_amount': 30919220, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 144, 'first_seen': 1760285763, 'matching_hash': 'b90602c7b9596cb3'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '950960749', 'validation_error': 'Invalid routing number checksum'}}}