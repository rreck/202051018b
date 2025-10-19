```json
{
  "id": "02be6ea87f050136",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293650,
  "host_pid": "9e6742732c60:1",
  "hash": "e4baede7148e15f88f2a270719b55749652010dfe76aafc1e7d91d8c2eef2d9a",
  "cid": "QmV1e4baede7148e15f88f2a270719b55749652010df",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293650,
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
      "evaluated_at": 1760293650
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
  "sig": "9a6efc0918cdd99232ab74837ce30d3f66df823809372ebd514bc739009240f8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594497049
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 223, 'threshold': 50, 'total_amount': 45677313, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 222, 'first_seen': 1760285763, 'matching_hash': 'c5255ffe70702a12'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '561028991', 'validation_error': 'Invalid routing number checksum'}}}