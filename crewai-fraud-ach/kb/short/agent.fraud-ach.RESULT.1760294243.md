```json
{
  "id": "d17ccd30eaa0ed85",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294243,
  "host_pid": "9e6742732c60:1",
  "hash": "ef576913db05afed68d3a07d6ba129ed98016b98bc813fea9a7f4aa9d063977c",
  "cid": "QmV1ef576913db05afed68d3a07d6ba129ed98016b98",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294243,
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
      "evaluated_at": 1760294243
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
  "sig": "a316f193cbde07a5ae95a1c9edadb4bb9b7e87f12b2db14bdaeea8f9a06e6311"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597735648
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 58933602, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285763, 'matching_hash': '529f1dc61ac58982'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '870312145', 'validation_error': 'Invalid routing number checksum'}}}