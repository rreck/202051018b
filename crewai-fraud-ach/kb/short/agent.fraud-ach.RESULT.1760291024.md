```json
{
  "id": "d8ab2e801f712a09",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291024,
  "host_pid": "9e6742732c60:1",
  "hash": "d6c1153ba0ec3b8273eaeeddc2f3081d15ddea28b5197c96526bf487863e7213",
  "cid": "QmV1d6c1153ba0ec3b8273eaeeddc2f3081d15ddea28",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291024,
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
      "evaluated_at": 1760291024
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
  "sig": "9b76da5eeebe54207a04daaf082fdf246e34d70bd26933a946f225354493c1df"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023207579
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 165, 'threshold': 50, 'total_amount': 59417820, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 164, 'first_seen': 1760285763, 'matching_hash': '07d0951e15487e7b'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '607486349', 'validation_error': 'Invalid routing number checksum'}}}