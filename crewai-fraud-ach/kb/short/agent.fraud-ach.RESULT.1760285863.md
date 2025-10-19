```json
{
  "id": "cbffa996a0dc4622",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285863,
  "host_pid": "9e6742732c60:1",
  "hash": "09cc9212511ef48e8049b10e010d171266a7da67a0b364a18705ab229ae52e5f",
  "cid": "QmV109cc9212511ef48e8049b10e010d171266a7da67",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285863,
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
      "evaluated_at": 1760285863
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
  "sig": "099af87a7eb91db47aa53e79c481e89a85299754c1b5807f98b19557c531a012"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009595856880
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 5, 'first_seen': 1760285763, 'matching_hash': '3e252270c9e333bc'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '561028991', 'validation_error': 'Invalid routing number checksum'}}}