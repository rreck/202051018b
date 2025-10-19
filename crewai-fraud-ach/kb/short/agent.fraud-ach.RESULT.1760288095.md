```json
{
  "id": "a12035a8cc9c1013",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288095,
  "host_pid": "9e6742732c60:1",
  "hash": "45e0604a83585561578f90808beda54e55ffb1af3c8b919b19a2e980e852cda6",
  "cid": "QmV145e0604a83585561578f90808beda54e55ffb1af",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288095,
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
      "evaluated_at": 1760288095
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
  "sig": "8061c62bcf1fd477c2138420e091acef8d4717a0f104fc509c01ec74c183d81d"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 107455396447712
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 82, 'threshold': 50, 'total_amount': 40766956, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 81, 'first_seen': 1760285765, 'matching_hash': 'bb26c320d6c9a382'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '107455391', 'validation_error': 'Invalid routing number checksum'}}}