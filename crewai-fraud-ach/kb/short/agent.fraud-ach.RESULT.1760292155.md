```json
{
  "id": "8b0ff4cee4f8d560",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292155,
  "host_pid": "9e6742732c60:1",
  "hash": "8c7876917cee3b2d14e5aa0e1819f7bd1dbd2868f851b21a8e4c845a7a39113f",
  "cid": "QmV18c7876917cee3b2d14e5aa0e1819f7bd1dbd2868",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292155,
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
      "evaluated_at": 1760292155
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
  "sig": "a925b435338256cbd0be05277c207a7bc4b3ea5abd512b2cee0f80f7a1e71c52"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241271841
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 191, 'threshold': 50, 'total_amount': 82506461, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 190, 'first_seen': 1760285764, 'matching_hash': '100dee2bbeee5c05'}}}