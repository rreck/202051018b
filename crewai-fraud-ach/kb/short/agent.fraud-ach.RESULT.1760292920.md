```json
{
  "id": "f2f2db65cc75697a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292920,
  "host_pid": "9e6742732c60:1",
  "hash": "c2485f379beb6f21be4474a893585ba239de9a48e87d4557b52cf4d833a50a9e",
  "cid": "QmV1c2485f379beb6f21be4474a893585ba239de9a48",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292920,
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
      "evaluated_at": 1760292920
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
  "sig": "a0959cbdcd96f2059fb82df807218b2f076b2d1a88356874431586b4428f4033"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591082294
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 208, 'threshold': 50, 'total_amount': 96607888, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 207, 'first_seen': 1760285763, 'matching_hash': 'b890dc886075e9be'}}} {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '294015854', 'validation_error': 'Invalid routing number checksum'}}}