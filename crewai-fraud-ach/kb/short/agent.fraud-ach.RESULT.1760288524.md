```json
{
  "id": "477752f744a8e42f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288524,
  "host_pid": "9e6742732c60:1",
  "hash": "e40f46b79d206665c1a5673ecb2172b69c21f9ebae0da4acfb370f8220f25043",
  "cid": "QmV1e40f46b79d206665c1a5673ecb2172b69c21f9eb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288524,
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
      "evaluated_at": 1760288524
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
  "sig": "e7128b3ffb458b704f3de3fd1a9814519ac492260d880f94b7eacc80db348909"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032712325
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 96, 'threshold': 50, 'total_amount': 34929696, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 95, 'first_seen': 1760285763, 'matching_hash': '06a9425dc3ac5c5b'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '614505622', 'validation_error': 'Invalid routing number checksum'}}}