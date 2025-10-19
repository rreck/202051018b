```json
{
  "id": "369c5e131f855ed0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287239,
  "host_pid": "9e6742732c60:1",
  "hash": "ff04797ab722ef89ad5db8c035704145375191b7d5194a8a5732de11e1f9a3e6",
  "cid": "QmV1ff04797ab722ef89ad5db8c035704145375191b7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287239,
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
      "evaluated_at": 1760287239
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
  "sig": "5c5702ee81b33af60de63a3220777868a9c107262f574b0509c8a7dd6e13009c"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 442437642525688
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 53, 'threshold': 50, 'total_amount': 11117015, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 52, 'first_seen': 1760285764, 'matching_hash': 'ad516aac642c681b'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '442437646', 'validation_error': 'Invalid routing number checksum'}}}