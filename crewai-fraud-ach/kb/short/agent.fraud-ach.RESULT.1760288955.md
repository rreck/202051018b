```json
{
  "id": "a3d8254ec3d72601",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288955,
  "host_pid": "9e6742732c60:1",
  "hash": "3c8050f22326a4fd7eac4fd93ba24b936fac17870e9937acb37b2ef7c16049b3",
  "cid": "QmV13c8050f22326a4fd7eac4fd93ba24b936fac1787",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288955,
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
      "evaluated_at": 1760288955
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "4d2b6a14bf048ed3f9e69de8f1345539d9e23d631ae76f4f701dbf53d4f55f32"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 442437642525688
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 109, 'threshold': 50, 'total_amount': 22863295, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 108, 'first_seen': 1760285764, 'matching_hash': 'ad516aac642c681b'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '442437646', 'validation_error': 'Invalid routing number checksum'}}}