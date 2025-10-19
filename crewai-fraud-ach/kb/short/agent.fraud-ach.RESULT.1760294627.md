```json
{
  "id": "92905c647b4729fa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294627,
  "host_pid": "9e6742732c60:1",
  "hash": "609b5e2da9d35a499dd5d45e7774c0aee223d0835d069d84d41b44599508ac25",
  "cid": "QmV1609b5e2da9d35a499dd5d45e7774c0aee223d083",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294627,
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
      "evaluated_at": 1760294627
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
  "sig": "f317abbe49705c660efcc2938e7a28291e0087c07e37f0ce344187f044075986"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591834365
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 93436905, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285765, 'matching_hash': 'c677ee5f465e30c5'}}}