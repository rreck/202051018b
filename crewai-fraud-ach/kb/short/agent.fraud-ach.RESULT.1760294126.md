```json
{
  "id": "8895f9c6cb7b6e7d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294126,
  "host_pid": "9e6742732c60:1",
  "hash": "d951c119fc5a66e3f0c282e8b3d5bcf5def83c25adc0f812e70a415a357a0ad7",
  "cid": "QmV1d951c119fc5a66e3f0c282e8b3d5bcf5def83c25",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294126,
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
      "evaluated_at": 1760294126
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
  "sig": "9dd8213d921a4f0d04db0dd1c8fb27d28592228784bfb2441a55c5a85dfabb40"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 051442861806700
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 98840120, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285765, 'matching_hash': '36501cb7899f5f80'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '051442869', 'validation_error': 'Invalid routing number checksum'}}}