```json
{
  "id": "60021812f2087110",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288372,
  "host_pid": "9e6742732c60:1",
  "hash": "c0c1113d63f37c32e348d6e2c75b5e734041a04cce3c2081d16f26b12975ffe7",
  "cid": "QmV1c0c1113d63f37c32e348d6e2c75b5e734041a04c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288372,
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
      "evaluated_at": 1760288372
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
  "sig": "c9944fe50f5e853be166631e9b499e97ebb0074f043aad225a417c43c54eda38"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592552790
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 91, 'threshold': 50, 'total_amount': 29852095, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 90, 'first_seen': 1760285764, 'matching_hash': 'c5daecdc9bc16873'}}}