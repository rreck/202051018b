```json
{
  "id": "8c513365c5aca9c4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289468,
  "host_pid": "9e6742732c60:1",
  "hash": "c12c34729406ae7f4b213126027588ad178a0ba53fbc86c17a85b423408ef62c",
  "cid": "QmV1c12c34729406ae7f4b213126027588ad178a0ba5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289468,
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
      "evaluated_at": 1760289468
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
  "sig": "55d73c162b27c3af80a6571afa2764d9d637a57b1c8e88c5a220bb678efa4396"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598880520
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 124, 'threshold': 50, 'total_amount': 23617536, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 123, 'first_seen': 1760285764, 'matching_hash': '9fe1b03994749115'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '164661952', 'validation_error': 'Invalid routing number checksum'}}}