```json
{
  "id": "ca63a3cd92afac6b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291117,
  "host_pid": "9e6742732c60:1",
  "hash": "b5c02074f31d3fc8e825c65a221366ee34458d80eb7c894f84a1515ede58e51b",
  "cid": "QmV1b5c02074f31d3fc8e825c65a221366ee34458d80",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291117,
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
      "evaluated_at": 1760291117
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
  "sig": "58882b40b314b1d89f1cb2174cb6da9aa14cae78b2899585f5b5ab628af7ad2f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156760115
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 167, 'threshold': 50, 'total_amount': 53568924, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 166, 'first_seen': 1760285764, 'matching_hash': '84a7174d04c2e814'}}}