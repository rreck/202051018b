```json
{
  "id": "dd0e8bfe06c3ccdd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287754,
  "host_pid": "9e6742732c60:1",
  "hash": "10e83e9e436770aaf9933b86a7344e5532d358d9a401bbf94083b0c88e19cb8f",
  "cid": "QmV110e83e9e436770aaf9933b86a7344e5532d358d9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287754,
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
      "evaluated_at": 1760287754
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
  "sig": "881792125bbcf34a1a3c9121a1ae25029531f72a63a451bf87c8ca7960922e69"
}
```

Fraud detected: duplicate_transaction (score: 88)
Transaction: 021000028860438
Details: {'velocity': {'fraud_detected': True, 'risk_score': 92, 'details': {'transaction_count': 71, 'threshold': 50, 'total_amount': 20839068, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 70, 'first_seen': 1760285763, 'matching_hash': '1ce58b471eab5597'}}}