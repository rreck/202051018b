```json
{
  "id": "9cca404d0587c086",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288233,
  "host_pid": "9e6742732c60:1",
  "hash": "3a27f08197617195f84c4f85785c7f93c8c8bab509cb3c2e5ad9b393b101e787",
  "cid": "QmV13a27f08197617195f84c4f85785c7f93c8c8bab5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288233,
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
      "evaluated_at": 1760288233
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
  "sig": "c673d470baaa6172ab6cf5d8b89b865b3b1b4bbf46b97975314ac7d8689325b3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152477967
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 87, 'threshold': 50, 'total_amount': 29610537, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 86, 'first_seen': 1760285763, 'matching_hash': '1f16fe6ce32cfab1'}}}aly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 8018549}}}