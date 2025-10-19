```json
{
  "id": "3ea6cf989b87e49e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294235,
  "host_pid": "9e6742732c60:1",
  "hash": "433258d66a716b6ec4b24e8658a6c14a31646bbf811cf49fbccc39df6e5b96e7",
  "cid": "QmV1433258d66a716b6ec4b24e8658a6c14a31646bbf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294235,
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
      "evaluated_at": 1760294235
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
  "sig": "b146f5f53bcd81fc68f8b527c27cc19fd360de1ac4a9d11b82020f05114d6967"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026682072
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 78664950, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285764, 'matching_hash': 'ef2983ea6f6c1303'}}}