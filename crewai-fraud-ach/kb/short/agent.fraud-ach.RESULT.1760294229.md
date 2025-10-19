```json
{
  "id": "8281e070468b16a2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294229,
  "host_pid": "9e6742732c60:1",
  "hash": "fbaebe23e110c8f0f077234bd4eb070a1d1d7040780045d81c4c8af93e717f57",
  "cid": "QmV1fbaebe23e110c8f0f077234bd4eb070a1d1d7040",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294229,
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
      "evaluated_at": 1760294229
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
  "sig": "c4f41e469f3843269f2ebd841f317fe0fdf49f9125077cf3b6bb799a1c96381a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022711139
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 100659312, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285763, 'matching_hash': '282a945486899803'}}}