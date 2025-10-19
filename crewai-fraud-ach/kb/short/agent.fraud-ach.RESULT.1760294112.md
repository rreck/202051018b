```json
{
  "id": "5e5559ce2b4b6c35",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294112,
  "host_pid": "9e6742732c60:1",
  "hash": "a726edc49765ed59d79b0f60e581a13b944fddf1b534d7cd3c9ce83e260dedc4",
  "cid": "QmV1a726edc49765ed59d79b0f60e581a13b944fddf1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294112,
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
      "evaluated_at": 1760294112
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
  "sig": "8a8f4c7d686a27186375891ad1f97b23e97a0e2944e6daa09f0ff7c69bf36746"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246611704
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 69018608, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285763, 'matching_hash': '524463c0aee194a0'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '667325181', 'validation_error': 'Invalid routing number checksum'}}}