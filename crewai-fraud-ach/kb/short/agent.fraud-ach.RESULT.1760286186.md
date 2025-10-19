```json
{
  "id": "06583d7f940d0967",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286186,
  "host_pid": "9e6742732c60:1",
  "hash": "5c7428d039364d9d3f103596c9872939dbd7c8b0d7a156c9ac2c7d1ddbbfa4bb",
  "cid": "QmV15c7428d039364d9d3f103596c9872939dbd7c8b0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286186,
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
      "evaluated_at": 1760286186
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
  "sig": "f524db32870095c25f39c6506782d49169dcf6d66193cbecf440e7a0d7394766"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201461436182
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 16, 'first_seen': 1760285765, 'matching_hash': 'd641045bf224534b'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '288759214', 'validation_error': 'Invalid routing number checksum'}}}