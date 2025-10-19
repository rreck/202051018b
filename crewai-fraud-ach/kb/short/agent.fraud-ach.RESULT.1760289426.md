```json
{
  "id": "db6b5f976e43af4b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289426,
  "host_pid": "9e6742732c60:1",
  "hash": "9c2fd6dfe88e23ba44936717e44e6c74305d51b2fc85afba5ae3bf3161602ab0",
  "cid": "QmV19c2fd6dfe88e23ba44936717e44e6c74305d51b2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289426,
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
      "evaluated_at": 1760289426
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
  "sig": "863667cba94c7ea1b2dd62ded86445a75b574ec2f286e181ba8307e7365f9e39"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022338434
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 123, 'threshold': 50, 'total_amount': 55339176, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 122, 'first_seen': 1760285763, 'matching_hash': '4c9dfd860457308a'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}