```json
{
  "id": "0eeeaa7cb4216f8f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287968,
  "host_pid": "9e6742732c60:1",
  "hash": "74a7f2cb67a4b06c411dccfcf0d39fc4349f812b6d2569ce1acf12c91850561e",
  "cid": "QmV174a7f2cb67a4b06c411dccfcf0d39fc4349f812b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287968,
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
      "evaluated_at": 1760287968
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
  "sig": "a9071558db7f47194e97dc29e72e8fb427a963cac8f0a6c247b2439fc57698b4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000023966417
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 78, 'threshold': 50, 'total_amount': 35477832, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 77, 'first_seen': 1760285764, 'matching_hash': 'bf59b19c5a8c3ed8'}}}