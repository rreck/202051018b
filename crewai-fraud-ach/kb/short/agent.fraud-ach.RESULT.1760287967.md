```json
{
  "id": "4a060a9663724a62",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287967,
  "host_pid": "9e6742732c60:1",
  "hash": "4bcaf074ac58b100bf23708f24891248038ac49aa8f64205c9a45a8e74adb7aa",
  "cid": "QmV14bcaf074ac58b100bf23708f24891248038ac49a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287967,
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
      "evaluated_at": 1760287967
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
  "sig": "12efc577617eb23d86ab87c0724de77c09802973bc4c60a14a4a07e3c07ce646"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 479377306721842
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 78, 'threshold': 50, 'total_amount': 25478076, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 77, 'first_seen': 1760285764, 'matching_hash': '9b6eff4280210a62'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '479377304', 'validation_error': 'Invalid routing number checksum'}}}