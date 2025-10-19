```json
{
  "id": "113a67ab2831bfb2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287222,
  "host_pid": "9e6742732c60:1",
  "hash": "fc49bd68447fe5cb3385dea795ee4032cc9f3c912651c54f4162fc7a7311c34d",
  "cid": "QmV1fc49bd68447fe5cb3385dea795ee4032cc9f3c91",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287222,
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
      "evaluated_at": 1760287222
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
  "sig": "74e676378489bf26302e96b82137e298b1a73b7873237cf6b1997a587fc79706"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 107455396447712
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 52, 'threshold': 50, 'total_amount': 25852216, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 51, 'first_seen': 1760285765, 'matching_hash': 'bb26c320d6c9a382'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '107455391', 'validation_error': 'Invalid routing number checksum'}}}