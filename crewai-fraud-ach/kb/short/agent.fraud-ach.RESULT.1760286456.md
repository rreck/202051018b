```json
{
  "id": "938100b39e31351e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286456,
  "host_pid": "9e6742732c60:1",
  "hash": "189f25e3ed6b31a09b6d3db48765b90fec23eab1b8e306836970150fa7ac0d3d",
  "cid": "QmV1189f25e3ed6b31a09b6d3db48765b90fec23eab1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286456,
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
      "evaluated_at": 1760286456
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
  "sig": "ea4f8c2d577fc39d4d8fa2cbf2733f3977cf30ffa4564151c23537f57ec146ff"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000038072034
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 25, 'first_seen': 1760285763, 'matching_hash': '336ae1a1ad6e821c'}}}ue, 'risk_score': 85, 'details': {'duplicate_count': 25, 'first_seen': 1760285763, 'matching_hash': '147c6cadc877e9f2'}}}g': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '398958456', 'validation_error': 'Invalid routing number checksum'}}}