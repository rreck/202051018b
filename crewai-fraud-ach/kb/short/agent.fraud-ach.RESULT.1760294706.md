```json
{
  "id": "27a563f4dd44faac",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294706,
  "host_pid": "9e6742732c60:1",
  "hash": "042305f2cc4f164e6ef48d7f618b1ae937612ac6fedcc9aac3b3c4cf45006a73",
  "cid": "QmV1042305f2cc4f164e6ef48d7f618b1ae937612ac6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294706,
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
      "evaluated_at": 1760294706
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
  "sig": "4974caa578c2ec8165a253360e4fcde93881e12f0d7d81900ff6f5bc1d8e1977"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 586667912036113
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 120114414, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285763, 'matching_hash': '105f91128dc7abfc'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '586667919', 'validation_error': 'Invalid routing number checksum'}}}