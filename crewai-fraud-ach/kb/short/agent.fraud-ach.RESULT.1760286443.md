```json
{
  "id": "a712c40a396d6b7a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286443,
  "host_pid": "9e6742732c60:1",
  "hash": "d44baab8039e9af39110f6965e247afd04323f0faa742d34e89fe8364257c817",
  "cid": "QmV1d44baab8039e9af39110f6965e247afd04323f0f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286443,
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
      "evaluated_at": 1760286443
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
  "sig": "4701425e35fa498c43d1a4eeace5402972f127595080f63e818a1e495bc2fcce"
}
```

Fraud detected: invalid_routing (score: 90)
Transaction: 507153179781967
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 24, 'first_seen': 1760285765, 'matching_hash': 'b9dbbc4d232307f2'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '507153176', 'validation_error': 'Invalid routing number checksum'}}}