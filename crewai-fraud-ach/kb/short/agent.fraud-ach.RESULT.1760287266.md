```json
{
  "id": "058b2d6f50ab7742",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287266,
  "host_pid": "9e6742732c60:1",
  "hash": "75d142eb23d367a20c04285f8fdc6583059db67a4962793e8502dbfaa1051184",
  "cid": "QmV175d142eb23d367a20c04285f8fdc6583059db67a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287266,
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
      "evaluated_at": 1760287266
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
  "sig": "11bd736aa2688419c6fe8629676e36ef9a0164e83845769db118acbd1fea15f1"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000246379487
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 54, 'threshold': 50, 'total_amount': 25844238, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 53, 'first_seen': 1760285764, 'matching_hash': 'aafc2265b0403e69'}}}