```json
{
  "id": "bcef4badd5ff29b6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288245,
  "host_pid": "9e6742732c60:1",
  "hash": "b58450a2b906d6bb676fdd4a9a57965fd259ec0596b09c4102e3244fb809a968",
  "cid": "QmV1b58450a2b906d6bb676fdd4a9a57965fd259ec05",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288245,
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
      "evaluated_at": 1760288245
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
  "sig": "bf9ce37eedc0139c5046cb5e5a87b44ae40f83256f206cbd602adf5f957e9aae"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 479377306721842
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 87, 'threshold': 50, 'total_amount': 28417854, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 86, 'first_seen': 1760285764, 'matching_hash': '9b6eff4280210a62'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '479377304', 'validation_error': 'Invalid routing number checksum'}}}