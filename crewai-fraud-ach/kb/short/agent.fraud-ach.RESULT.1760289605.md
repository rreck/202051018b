```json
{
  "id": "2454b5043be11855",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289605,
  "host_pid": "9e6742732c60:1",
  "hash": "64287f8a54f14297c055b74644d5ca87093c57e1286335cc558e83db2b6c77fe",
  "cid": "QmV164287f8a54f14297c055b74644d5ca87093c57e1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289605,
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
      "evaluated_at": 1760289605
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
  "sig": "c3950121dcb1b70051c0c0abef35e93fb340c946c635668c9cfd32fe15601757"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 824845893834283
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 128, 'threshold': 50, 'total_amount': 35586688, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 127, 'first_seen': 1760285764, 'matching_hash': '751a36f41382ae06'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '824845890', 'validation_error': 'Invalid routing number checksum'}}}