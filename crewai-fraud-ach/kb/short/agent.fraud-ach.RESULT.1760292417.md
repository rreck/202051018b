```json
{
  "id": "b250853593afccca",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292417,
  "host_pid": "9e6742732c60:1",
  "hash": "826e5f0d3bd2c200134906022b3977198327f9d35eacad9631e6c98fdf079097",
  "cid": "QmV1826e5f0d3bd2c200134906022b3977198327f9d3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292417,
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
      "evaluated_at": 1760292417
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
  "sig": "f4cc0d7c5d90124e40337019d83dbd61d235da5599ca150c18b604a7a03d32ab"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151200756
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 197, 'threshold': 50, 'total_amount': 32035943, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 196, 'first_seen': 1760285763, 'matching_hash': 'e0249734267f8906'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '443655354', 'validation_error': 'Invalid routing number checksum'}}}