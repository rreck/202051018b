```json
{
  "id": "7e55ef8554737bd9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293654,
  "host_pid": "9e6742732c60:1",
  "hash": "14c1f424973360814a1dd9bc9a03e5c861623e0ff449d54f8fec9292431c922a",
  "cid": "QmV114c1f424973360814a1dd9bc9a03e5c861623e0f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293654,
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
      "evaluated_at": 1760293654
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
  "sig": "18001224903f74d54457e16547edd5b0592b1ff61b4c439ee42615bd581dc16c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462101683
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 223, 'threshold': 50, 'total_amount': 73962633, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 222, 'first_seen': 1760285763, 'matching_hash': 'e66600e2d7fa312e'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '244096997', 'validation_error': 'Invalid routing number checksum'}}}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}