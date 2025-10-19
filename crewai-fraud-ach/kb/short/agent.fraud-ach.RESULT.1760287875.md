```json
{
  "id": "ea7a5b0088e10548",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287875,
  "host_pid": "9e6742732c60:1",
  "hash": "3d15dd345723ee73119e1e1fbe12877f400060e9ccabd9c600b0a2e1bb24c038",
  "cid": "QmV13d15dd345723ee73119e1e1fbe12877f400060e9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287875,
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
      "evaluated_at": 1760287875
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
  "sig": "11356b1f365eb663fcbeb64d78d211a1ef8c475d2b41c042b090632ef0e8e8bb"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 818590551241151
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 75, 'threshold': 50, 'total_amount': 19130475, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 74, 'first_seen': 1760285763, 'matching_hash': '902b02e4e6ce46b6'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '818590557', 'validation_error': 'Invalid routing number checksum'}}}