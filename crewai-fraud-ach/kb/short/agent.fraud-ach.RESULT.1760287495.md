```json
{
  "id": "b74ddf8724717ea9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287495,
  "host_pid": "9e6742732c60:1",
  "hash": "82b7b539a49dcf2e51f62ea54e4b9bd34c5724af6e5f3efe3d4488e54c8f28c2",
  "cid": "QmV182b7b539a49dcf2e51f62ea54e4b9bd34c5724af",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287495,
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
      "evaluated_at": 1760287495
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
  "sig": "b686014fc2c725e2a261417f54a583f70320b44afdec070fbc3f0a62aeac0431"
}
```

Fraud detected: invalid_routing (score: 84)
Transaction: 491975137325012
Details: {'velocity': {'fraud_detected': True, 'risk_score': 74, 'details': {'transaction_count': 62, 'threshold': 50, 'total_amount': 18270904, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 61, 'first_seen': 1760285763, 'matching_hash': '2178be3eb8984b5a'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '491975133', 'validation_error': 'Invalid routing number checksum'}}}