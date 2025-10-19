```json
{
  "id": "887789a48b391bf1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287760,
  "host_pid": "9e6742732c60:1",
  "hash": "d2f3bd23ce318516d880cf9fd582ab39d981c07f3a4cb6ddbad4f82af8fcd523",
  "cid": "QmV1d2f3bd23ce318516d880cf9fd582ab39d981c07f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287760,
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
      "evaluated_at": 1760287760
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
  "sig": "ed5e42e080fba47f24b1a548cd2a9ec78d8381c1c843ba4ccada25993329bbfc"
}
```

Fraud detected: duplicate_transaction (score: 88)
Transaction: 044000033751291
Details: {'velocity': {'fraud_detected': True, 'risk_score': 92, 'details': {'transaction_count': 71, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 70, 'first_seen': 1760285765, 'matching_hash': '04859aaf1143bd8f'}}}