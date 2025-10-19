```json
{
  "id": "310a12e9810cdb89",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286910,
  "host_pid": "9e6742732c60:1",
  "hash": "0508521d9ae5ad7619263d5b93eb8f32c65c6b0dfe774bba4715c8f1ad645d8b",
  "cid": "QmV10508521d9ae5ad7619263d5b93eb8f32c65c6b0d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286910,
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
      "evaluated_at": 1760286910
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "d23286c83846ac9d44662436230ede5dfabb7d1087c7f686f36a875ed9823f2b"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 021000022243877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10250000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 40, 'first_seen': 1760285765, 'matching_hash': '9c2417d6ee361cba'}}}