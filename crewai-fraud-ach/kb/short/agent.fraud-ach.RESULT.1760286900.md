```json
{
  "id": "d92cc5f057ad9777",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286900,
  "host_pid": "9e6742732c60:1",
  "hash": "17c98232a74d3bc9fdbbe9c3d6993a21d23d7af71e03afb2053fbfd9463817aa",
  "cid": "QmV117c98232a74d3bc9fdbbe9c3d6993a21d23d7af7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286900,
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
      "evaluated_at": 1760286900
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
  "sig": "d76c65dcb9287b64032913b921ecc020c0895ff2a567f94e4a9d916d60d56ace"
}
```

Fraud detected: invalid_routing (score: 90)
Transaction: 033505362547520
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 40, 'first_seen': 1760285763, 'matching_hash': '3154a67bf8f8af44'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '033505362', 'validation_error': 'Invalid routing number checksum'}}}