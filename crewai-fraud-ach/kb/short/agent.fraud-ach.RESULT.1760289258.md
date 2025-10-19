```json
{
  "id": "9252060f19654be3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289258,
  "host_pid": "9e6742732c60:1",
  "hash": "ab64bdace053b28f1782ed6a730a5f837cf3317f753c11ec50a0ea07d03c2ac9",
  "cid": "QmV1ab64bdace053b28f1782ed6a730a5f837cf3317f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289258,
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
      "evaluated_at": 1760289258
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
  "sig": "032028ebf9b3d3a0d371eaeba2ec5e50be4be58f372be0562365a6c2113a50ea"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 649278780553328
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 118, 'threshold': 50, 'total_amount': 27383552, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 117, 'first_seen': 1760285765, 'matching_hash': 'c666b8c882e80c0b'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '649278788', 'validation_error': 'Invalid routing number checksum'}}}