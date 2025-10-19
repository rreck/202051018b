```json
{
  "id": "ad1018582ef2d15a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287585,
  "host_pid": "9e6742732c60:1",
  "hash": "78cf442848419092a29016138f23f0c52cd4677a79bccb3369949d19ec7c93a0",
  "cid": "QmV178cf442848419092a29016138f23f0c52cd4677a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287585,
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
      "evaluated_at": 1760287585
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
  "sig": "b3cba72126a13a45dda6132a8ab522cfa6b05705c97d13ee667b6229c0b19776"
}
```

Fraud detected: invalid_routing (score: 86)
Transaction: 011137004104696
Details: {'velocity': {'fraud_detected': True, 'risk_score': 80, 'details': {'transaction_count': 65, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 64, 'first_seen': 1760285765, 'matching_hash': 'b4a76c6b789f42f2'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '011137004', 'validation_error': 'Invalid routing number checksum'}}}