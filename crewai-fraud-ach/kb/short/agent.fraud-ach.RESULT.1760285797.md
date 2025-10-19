```json
{
  "id": "b1db22a9462bf5d6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285797,
  "host_pid": "9e6742732c60:1",
  "hash": "d00def88cb04237624f8b92bbe5389215bc6be4dc9a98f869e30c21a9949de53",
  "cid": "QmV1d00def88cb04237624f8b92bbe5389215bc6be4d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285797,
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
      "evaluated_at": 1760285797
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
  "sig": "683200a6b5ad48d12d3d351d3e0091319383ba3e913dc2755b2f7110bf69bf32"
}
```

Fraud detected: invalid_routing (score: 90)
Transaction: 085520768954692
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 2, 'first_seen': 1760285763, 'matching_hash': '4f8cdcee5609bbf1'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '085520764', 'validation_error': 'Invalid routing number checksum'}}}