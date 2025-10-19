```json
{
  "id": "ef0873ae2cb7ba0d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288047,
  "host_pid": "9e6742732c60:1",
  "hash": "c3aac9f4560dbfe38c3b216b9cb9406fce52bcbff1f6ef651d4f7657b329e254",
  "cid": "QmV1c3aac9f4560dbfe38c3b216b9cb9406fce52bcbf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288047,
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
      "evaluated_at": 1760288047
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
  "sig": "57864611eb5119a1934a5fd78b513a1ae5f3c9edf535e048a1857b40bfe843bf"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 730896563459202
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 81, 'threshold': 50, 'total_amount': 29079567, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 80, 'first_seen': 1760285763, 'matching_hash': 'b6a475fea2d998c5'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '730896563', 'validation_error': 'Invalid routing number checksum'}}}ower': -2106683.5, 'upper': 4084502.5}, 'amount': 8542478}}}