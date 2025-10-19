```json
{
  "id": "4662f201c95e797e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291994,
  "host_pid": "9e6742732c60:1",
  "hash": "da432983f2339cda39fb9244e121b907c55b257f0b4882bc0455ffd28b71f0e7",
  "cid": "QmV1da432983f2339cda39fb9244e121b907c55b257f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291994,
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
      "evaluated_at": 1760291994
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
  "sig": "ac967e5ee096dc98b27acae805df66a5516493ee8a1cfdefd83fc13e194cd381"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038829903
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 188, 'threshold': 50, 'total_amount': 14655728, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 187, 'first_seen': 1760285763, 'matching_hash': 'dff748e22041369e'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '987899137', 'validation_error': 'Invalid routing number checksum'}}}