```json
{
  "id": "d67dcde4e6efa76a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285915,
  "host_pid": "9e6742732c60:1",
  "hash": "96744f44bba35b392e75514ebb162bd6d7fe70f0282a812dd4b7f2aa791eae95",
  "cid": "QmV196744f44bba35b392e75514ebb162bd6d7fe70f0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285915,
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
      "evaluated_at": 1760285915
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
  "sig": "ed21a55d57e8328928156a137b3cd121f5798a10bab933c0a3386e63960f5ae8"
}
```

Fraud detected: invalid_routing (score: 90)
Transaction: 607486347609576
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 7, 'first_seen': 1760285763, 'matching_hash': '01e47067eb24b5e9'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '607486349', 'validation_error': 'Invalid routing number checksum'}}}