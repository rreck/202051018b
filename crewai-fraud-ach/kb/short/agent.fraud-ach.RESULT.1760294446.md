```json
{
  "id": "c7e053ca79de9a54",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294446,
  "host_pid": "9e6742732c60:1",
  "hash": "517ad54e838ab2b8ce44b4d1fec71dbb295c5dd272dbc33fd24ac20ff95dea3e",
  "cid": "QmV1517ad54e838ab2b8ce44b4d1fec71dbb295c5dd2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294446,
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
      "evaluated_at": 1760294446
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
  "sig": "a9d0f99a376f7e96f8e619b4d3ba25f97bc2119a01bed6b75b6bed2f2d4395aa"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 164661958921180
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 55726034, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285763, 'matching_hash': '1848c81652336fb1'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '164661952', 'validation_error': 'Invalid routing number checksum'}}}