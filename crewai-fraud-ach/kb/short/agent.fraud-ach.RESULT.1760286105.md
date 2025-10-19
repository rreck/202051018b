```json
{
  "id": "a8662c7125a5c1de",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286105,
  "host_pid": "9e6742732c60:1",
  "hash": "504b9778ec16046b9efe6568463963b7b4da4a3cccd501e9158d0539d63297b9",
  "cid": "QmV1504b9778ec16046b9efe6568463963b7b4da4a3c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286105,
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
      "evaluated_at": 1760286105
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
  "sig": "4cf7f538da3fbc7656aaa9369fa1383614ae7661508521d30de1ca72fdbb6745"
}
```

Fraud detected: invalid_routing (score: 90)
Transaction: 507153179781967
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 13, 'first_seen': 1760285765, 'matching_hash': 'b9dbbc4d232307f2'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '507153176', 'validation_error': 'Invalid routing number checksum'}}}