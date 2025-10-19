```json
{
  "id": "eff06d45bdc29ab7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292128,
  "host_pid": "9e6742732c60:1",
  "hash": "732bd300aec20322abd4bf095e1028d60906f6a4fb3b8a0cbc978455a5b32499",
  "cid": "QmV1732bd300aec20322abd4bf095e1028d60906f6a4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292128,
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
      "evaluated_at": 1760292128
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
  "sig": "4b771f5e28784811b29d0f4555b2e939313ceeeffff24f68305850763d4c907f"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 929669860929959
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 191, 'threshold': 50, 'total_amount': 40108281, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 190, 'first_seen': 1760285763, 'matching_hash': 'bbfcfb9a6aef8521'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '929669867', 'validation_error': 'Invalid routing number checksum'}}}