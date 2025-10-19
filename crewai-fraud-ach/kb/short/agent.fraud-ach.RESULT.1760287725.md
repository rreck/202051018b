```json
{
  "id": "c093dec083295411",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287725,
  "host_pid": "9e6742732c60:1",
  "hash": "581170df93ce28712c189ad56e8311ef3657ed0663dbb27b135e379f14799097",
  "cid": "QmV1581170df93ce28712c189ad56e8311ef3657ed06",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287725,
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
      "evaluated_at": 1760287725
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
  "sig": "3b754c7803a6ac89ccdaba35dd7b500faccd2b6faec4fdb5e7d17857a92a1977"
}
```

Fraud detected: duplicate_transaction (score: 87)
Transaction: 021000020048209
Details: {'velocity': {'fraud_detected': True, 'risk_score': 90, 'details': {'transaction_count': 70, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 69, 'first_seen': 1760285765, 'matching_hash': '08bd6998776e568a'}}}