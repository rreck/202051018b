```json
{
  "id": "5bc8bd05c98b598e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290783,
  "host_pid": "9e6742732c60:1",
  "hash": "3edbf795c880779138cd8a9fea1120cb6e5c92b4a4f95308ddb26bda5d0a0c17",
  "cid": "QmV13edbf795c880779138cd8a9fea1120cb6e5c92b4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290783,
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
      "evaluated_at": 1760290783
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
  "sig": "41d3f51ebb8c1fde8ee9422b9231516f62239c5e81815b663e788c6b1d7feba6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246221982
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 159, 'threshold': 50, 'total_amount': 37001049, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 158, 'first_seen': 1760285763, 'matching_hash': '5c0c0fe7ab2d6845'}}}