```json
{
  "id": "0029bd258222eeff",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286240,
  "host_pid": "9e6742732c60:1",
  "hash": "54c1151fcc4febffe7b7772185510a768ec2344a1146efd1b0d2af1c20de4f21",
  "cid": "QmV154c1151fcc4febffe7b7772185510a768ec2344a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286240,
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
      "evaluated_at": 1760286240
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
  "sig": "dc3bf43925a01d100c69fd49f499cdad90808aefcbf3e00728f2e017531eb643"
}
```

Fraud detected: invalid_routing (score: 90)
Transaction: 060557484693193
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 18, 'first_seen': 1760285763, 'matching_hash': 'db8aeeee2135ece1'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '060557489', 'validation_error': 'Invalid routing number checksum'}}}