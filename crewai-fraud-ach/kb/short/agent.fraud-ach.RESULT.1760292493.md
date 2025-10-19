```json
{
  "id": "27051ff8129d659b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292493,
  "host_pid": "9e6742732c60:1",
  "hash": "f61c8702ba9538df882eedced6444e12d70f87bc9ec3eff2deabd86c2477fcb1",
  "cid": "QmV1f61c8702ba9538df882eedced6444e12d70f87bc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292493,
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
      "evaluated_at": 1760292493
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
  "sig": "ec209cfb59f10a3177443aa685d7969f02622ddb9ff5168dc4d9ff7ee3dfac28"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 987899138590267
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 199, 'threshold': 50, 'total_amount': 88398785, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 198, 'first_seen': 1760285763, 'matching_hash': '4a74fde2b8c56926'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '987899137', 'validation_error': 'Invalid routing number checksum'}}}