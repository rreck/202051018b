```json
{
  "id": "d71a5ca3e3283f75",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290809,
  "host_pid": "9e6742732c60:1",
  "hash": "079034d457901517d87c8c49bcf4072153a88a6632cfdead76165d94e59f7eb9",
  "cid": "QmV1079034d457901517d87c8c49bcf4072153a88a66",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290809,
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
      "evaluated_at": 1760290809
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
  "sig": "91bde1decd3cc32c004c2537092bca5a36d86e9e9159e3e2307aa7b281097b8b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271052795
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 160, 'threshold': 50, 'total_amount': 35297280, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 159, 'first_seen': 1760285763, 'matching_hash': '457d955844db0007'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '987899137', 'validation_error': 'Invalid routing number checksum'}}}