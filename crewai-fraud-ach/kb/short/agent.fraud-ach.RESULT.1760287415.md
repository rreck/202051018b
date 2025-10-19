```json
{
  "id": "8dd6cab00f883581",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287415,
  "host_pid": "9e6742732c60:1",
  "hash": "09f3fb99023600a90c5ee5e938553a0e528f39bf50ce40cf3554ee9b745e7662",
  "cid": "QmV109f3fb99023600a90c5ee5e938553a0e528f39bf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287415,
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
      "evaluated_at": 1760287415
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
  "sig": "e4eb20e75fc0e4aad43e029f9eb52cbb0d2f9fd360ed3479013f4c11d0c8d850"
}
```

Fraud detected: invalid_routing (score: 82)
Transaction: 011137004104696
Details: {'velocity': {'fraud_detected': True, 'risk_score': 68, 'details': {'transaction_count': 59, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 58, 'first_seen': 1760285765, 'matching_hash': 'b4a76c6b789f42f2'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '011137004', 'validation_error': 'Invalid routing number checksum'}}}