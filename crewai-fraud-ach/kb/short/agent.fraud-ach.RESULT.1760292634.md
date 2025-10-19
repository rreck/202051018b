```json
{
  "id": "990d79c8dd483692",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292634,
  "host_pid": "9e6742732c60:1",
  "hash": "f14068913e13390b9df0caf0a99fe8a7aae36b060b0eccb42ed58ecc6251bb94",
  "cid": "QmV1f14068913e13390b9df0caf0a99fe8a7aae36b06",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292634,
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
      "evaluated_at": 1760292634
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
  "sig": "467508d01784ca3fff5a06d422bfd9f0a0d4603fb4f617af4841949f5d7afac6"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 261425243879882
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 202, 'threshold': 50, 'total_amount': 66730094, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 201, 'first_seen': 1760285763, 'matching_hash': 'bea146cfc71ce9bb'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '261425248', 'validation_error': 'Invalid routing number checksum'}}}nds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 7365830}}}