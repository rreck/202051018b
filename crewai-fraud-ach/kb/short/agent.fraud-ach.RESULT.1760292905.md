```json
{
  "id": "7d8142585933e547",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292905,
  "host_pid": "9e6742732c60:1",
  "hash": "bd9a176a2bfc9ef1357f33856a61fb6c359939957cd309abce8403d3d6482ea5",
  "cid": "QmV1bd9a176a2bfc9ef1357f33856a61fb6c35993995",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292905,
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
      "evaluated_at": 1760292905
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
  "sig": "eab32492dcd555e2ebc13cb1cfef3538a1a5679faa42f7204fec55fd6ae6c501"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243970709
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 207, 'threshold': 50, 'total_amount': 18332748, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 206, 'first_seen': 1760285765, 'matching_hash': '886d04c9297a738f'}}}