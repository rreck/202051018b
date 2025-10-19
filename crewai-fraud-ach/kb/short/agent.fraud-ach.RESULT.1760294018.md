```json
{
  "id": "01f66496e3c54573",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294018,
  "host_pid": "9e6742732c60:1",
  "hash": "36e8d9c35cccbf4ea87d698190bd8f6ddc0869515475d25f23541360a977ba63",
  "cid": "QmV136e8d9c35cccbf4ea87d698190bd8f6ddc086951",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294018,
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
      "evaluated_at": 1760294018
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
  "sig": "5ee7e5d4bd00147edb7657292c4084e1c748fce085c22ea8a3d6ec19abe3eada"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 304701772219564
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 54975750, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285764, 'matching_hash': '19ec134c2c5b9271'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '304701776', 'validation_error': 'Invalid routing number checksum'}}}nds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9245331}}}