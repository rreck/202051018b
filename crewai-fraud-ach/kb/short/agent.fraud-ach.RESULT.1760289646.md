```json
{
  "id": "326e6898af1eb7ad",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289646,
  "host_pid": "9e6742732c60:1",
  "hash": "b020e8b442d16862132b86d0687e139e58527582472307647e14b0f28694468c",
  "cid": "QmV1b020e8b442d16862132b86d0687e139e58527582",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289646,
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
      "evaluated_at": 1760289646
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
  "sig": "4d39ad7a5b2cbb9ac018bb22828e0058cb47b45873cfc0e5138e9f2696f75653"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026302865
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 129, 'threshold': 50, 'total_amount': 38772756, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 128, 'first_seen': 1760285763, 'matching_hash': '15ebb46c9afca80b'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '442437646', 'validation_error': 'Invalid routing number checksum'}}}