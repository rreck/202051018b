```json
{
  "id": "853ea85f04d56f12",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288950,
  "host_pid": "9e6742732c60:1",
  "hash": "bde8ea9ed1812d357fe9add9d75d26bb761b9c125f5781d80ba7edbeb2e45720",
  "cid": "QmV1bde8ea9ed1812d357fe9add9d75d26bb761b9c12",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288950,
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
      "evaluated_at": 1760288950
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
  "sig": "fcda13871cef4f15f9df195cd559517406f0a522f07871c0b0c07eb2a0f3e0bc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029122182
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 109, 'threshold': 50, 'total_amount': 10900000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 108, 'first_seen': 1760285763, 'matching_hash': '6eeeaf20a2fbd10d'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '950960749', 'validation_error': 'Invalid routing number checksum'}}}