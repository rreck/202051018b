```json
{
  "id": "4709dd821af049ca",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292970,
  "host_pid": "9e6742732c60:1",
  "hash": "31d10069aa756a56ae5dc79b6325c0c07fe0324b9673f0ce6bf5b6e90a32d890",
  "cid": "QmV131d10069aa756a56ae5dc79b6325c0c07fe0324b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292970,
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
      "evaluated_at": 1760292970
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
  "sig": "ee20c7acaf0dce1ff864a5a31ef3cdd9b4df83bd3e7112432b0ae4bddfba7bb2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278631812
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 209, 'threshold': 50, 'total_amount': 39672798, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 208, 'first_seen': 1760285763, 'matching_hash': 'e154fa328ed40444'}}}