```json
{
  "id": "09ebd9af66ea5183",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286130,
  "host_pid": "9e6742732c60:1",
  "hash": "bf167276c685b3eabe7a0117d93a3a7acfbb472cce592deebc57538e392d5b1d",
  "cid": "QmV1bf167276c685b3eabe7a0117d93a3a7acfbb472c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286130,
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
      "evaluated_at": 1760286130
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
  "sig": "37be63212266802965242727f62c4e238600c06966acf63306a65dd6bdde97e4"
}
```

Fraud detected: invalid_routing (score: 90)
Transaction: 160455148414817
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 14, 'first_seen': 1760285764, 'matching_hash': 'c57b46b00801b500'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '160455141', 'validation_error': 'Invalid routing number checksum'}}}