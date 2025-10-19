```json
{
  "id": "08cf566439b2d81a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292758,
  "host_pid": "9e6742732c60:1",
  "hash": "b7b05adc9700b03b015b1a45664a207d312903636f52b808e03a3a9ede080ee2",
  "cid": "QmV1b7b05adc9700b03b015b1a45664a207d31290363",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292758,
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
      "evaluated_at": 1760292758
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
  "sig": "6e9320a96405149c00d76d7963f44634c5935b69571368c8a8a814bad87ead4a"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 009592678117470
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 204, 'threshold': 50, 'total_amount': 24707256, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 203, 'first_seen': 1760285764, 'matching_hash': 'f5249213623024b2'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '009592679', 'validation_error': 'Invalid routing number checksum'}}}