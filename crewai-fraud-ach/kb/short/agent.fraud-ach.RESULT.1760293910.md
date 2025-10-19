```json
{
  "id": "078fb195d2eafd1d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293910,
  "host_pid": "9e6742732c60:1",
  "hash": "7a6f7d4e250c4d58bf91bb7ce00b104df51a0d9fc3896de0f122a4cf637b14ab",
  "cid": "QmV17a6f7d4e250c4d58bf91bb7ce00b104df51a0d9f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293910,
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
      "evaluated_at": 1760293910
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
  "sig": "f3bdbdcde53b16851efa8836e49564e7aa3dd7a596e224062df9c279708ef955"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461090276
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 228, 'threshold': 50, 'total_amount': 59083920, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 227, 'first_seen': 1760285763, 'matching_hash': '697ecd0ef10c625b'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '041887155', 'validation_error': 'Invalid routing number checksum'}}}