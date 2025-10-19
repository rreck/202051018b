```json
{
  "id": "ca0c5deaebd08532",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294914,
  "host_pid": "9e6742732c60:1",
  "hash": "cb691970bb849d82c22eaa186685b1147a80a434c967f29d639e253cfd2664d5",
  "cid": "QmV1cb691970bb849d82c22eaa186685b1147a80a434",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294914,
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
      "evaluated_at": 1760294915
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
  "sig": "c760302b7029f1a87f2ee41f526a6f13e7461aa21350822dcd086b2dd8557799"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 561028999821965
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 247, 'threshold': 50, 'total_amount': 34577283, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 246, 'first_seen': 1760285763, 'matching_hash': '09f745cfd1242827'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '561028991', 'validation_error': 'Invalid routing number checksum'}}}