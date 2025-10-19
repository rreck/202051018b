```json
{
  "id": "57cb70200d87378a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289153,
  "host_pid": "9e6742732c60:1",
  "hash": "d032fd7f0bf43c78a3a69dc88311369a0b84488ec4911f2bfff932c4bf8b0f64",
  "cid": "QmV1d032fd7f0bf43c78a3a69dc88311369a0b84488e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289153,
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
      "evaluated_at": 1760289153
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
  "sig": "a22ff1d84fddf78281c8b9af1b6a2b0d5ca647646a157bc2413a22e9a1e397b8"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 542300578273472
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 115, 'threshold': 50, 'total_amount': 28666970, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 114, 'first_seen': 1760285764, 'matching_hash': '6580c6d1de434ae0'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '542300570', 'validation_error': 'Invalid routing number checksum'}}}