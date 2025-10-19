```json
{
  "id": "f4425e03faea0ab1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291440,
  "host_pid": "9e6742732c60:1",
  "hash": "4eb198164b16e1a3012ad07f3cb3cf93e3701810119e06d16e8255106fe55531",
  "cid": "QmV14eb198164b16e1a3012ad07f3cb3cf93e3701810",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291440,
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
      "evaluated_at": 1760291440
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
  "sig": "fac3113fdc8a5ad6481cecc7772f3a3f03c89ea70c59e4888c2400a58d6977bb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153135421
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 175, 'threshold': 50, 'total_amount': 66786300, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 174, 'first_seen': 1760285763, 'matching_hash': '4394c86a949e27d6'}}}