```json
{
  "id": "fd3a133d97cab1e8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291542,
  "host_pid": "9e6742732c60:1",
  "hash": "521dfd9fa1a89f0ffb24b210f159e7f8771524fa64d9a60c4207aebc14103671",
  "cid": "QmV1521dfd9fa1a89f0ffb24b210f159e7f8771524fa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291542,
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
      "evaluated_at": 1760291542
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
  "sig": "a31a57e996b824a6f214c02dc7e2c4094373a8c4ffd456bf7060e10ae5dace2a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270344488
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 177, 'threshold': 50, 'total_amount': 47215281, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 176, 'first_seen': 1760285764, 'matching_hash': 'ec3de169da630728'}}}