```json
{
  "id": "2782f9191042dc26",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288273,
  "host_pid": "9e6742732c60:1",
  "hash": "4e53cd040cbcb86764d9cdb33a78bab3d26411096d4f49c0dd7b01d7f3a4c507",
  "cid": "QmV14e53cd040cbcb86764d9cdb33a78bab3d2641109",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288273,
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
      "evaluated_at": 1760288273
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
  "sig": "b5b95a9a9f2b8ef3adb59116ba45db240b4011227d72955d8a732682787e1941"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 676666911893287
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 88, 'threshold': 50, 'total_amount': 34316304, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 87, 'first_seen': 1760285763, 'matching_hash': '67218afda9e45d8d'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '676666915', 'validation_error': 'Invalid routing number checksum'}}}