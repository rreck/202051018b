```json
{
  "id": "6953cc8eeb49a6bc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290534,
  "host_pid": "9e6742732c60:1",
  "hash": "70a8248fd39582fd962845982f2d4222ad5423d192028ec861e1bef663c7e815",
  "cid": "QmV170a8248fd39582fd962845982f2d4222ad5423d1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290534,
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
      "evaluated_at": 1760290534
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "45e8ce1a210266e86c903bd3d2268d8a6b7189604ff603343479e392d6f2c5c3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244267355
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 153, 'threshold': 50, 'total_amount': 23005080, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 152, 'first_seen': 1760285763, 'matching_hash': '9a2cfa03d6a38585'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '261425248', 'validation_error': 'Invalid routing number checksum'}}}