```json
{
  "id": "4c937890045c7d38",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290267,
  "host_pid": "9e6742732c60:1",
  "hash": "317a276fccf31de87849ce75536da1ff2be53c41a84c035b8142184286d8e482",
  "cid": "QmV1317a276fccf31de87849ce75536da1ff2be53c41",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290267,
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
      "evaluated_at": 1760290267
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
  "sig": "17efb0184a3be3ea8785109eafe53ca3828acaf61432d7776cedfad4b5a85904"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038495907
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 146, 'threshold': 50, 'total_amount': 39712292, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 145, 'first_seen': 1760285763, 'matching_hash': '3a0df0e30691ba23'}}}