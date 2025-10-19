```json
{
  "id": "3eaa9c896430ab36",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288267,
  "host_pid": "9e6742732c60:1",
  "hash": "c4c55f91f7500c71fd0cdd207ba34b027cd41168b73aee156a8532b99614b7d8",
  "cid": "QmV1c4c55f91f7500c71fd0cdd207ba34b027cd41168",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288267,
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
      "evaluated_at": 1760288267
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
  "sig": "17d340f9cee6cfcf3c0c8f5f30ebe44636204aa85c0640eccf0dc50aac067b92"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158076407
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 88, 'threshold': 50, 'total_amount': 13071960, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 87, 'first_seen': 1760285763, 'matching_hash': 'bd01239b3993ff64'}}}