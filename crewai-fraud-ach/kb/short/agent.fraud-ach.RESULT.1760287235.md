```json
{
  "id": "d318dc937a94b8a9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287235,
  "host_pid": "9e6742732c60:1",
  "hash": "d4f0b93298426c1f47e943dadb4b968ffc78941dff7bc9ddc1a77bc31d926517",
  "cid": "QmV1d4f0b93298426c1f47e943dadb4b968ffc78941d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287235,
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
      "evaluated_at": 1760287235
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "97fb197a660385beb2a561af1a89ef097737baa93ef43fec7ebc8b472a730d8c"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201462461467
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 53, 'threshold': 50, 'total_amount': 19594153, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 52, 'first_seen': 1760285763, 'matching_hash': '257546013422e30a'}}}g': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '568426909', 'validation_error': 'Invalid routing number checksum'}}}