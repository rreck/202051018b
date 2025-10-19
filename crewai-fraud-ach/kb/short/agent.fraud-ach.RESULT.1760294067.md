```json
{
  "id": "3048466d1dca0047",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294067,
  "host_pid": "9e6742732c60:1",
  "hash": "1a6a08723a0e37464d29c5a1f471e406ae8fb83df2c65e95d9cac11e3ed93fce",
  "cid": "QmV11a6a08723a0e37464d29c5a1f471e406ae8fb83d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294067,
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
      "evaluated_at": 1760294067
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
  "sig": "3eea2daa699d995b0e9ce52307524cc7465e16664818489c832725b83cdf3305"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 182683956982385
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 34568457, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285764, 'matching_hash': '0eeac2a2909779e4'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '182683957', 'validation_error': 'Invalid routing number checksum'}}}