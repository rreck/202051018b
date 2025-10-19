```json
{
  "id": "b0a95edc52df0e6d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288789,
  "host_pid": "9e6742732c60:1",
  "hash": "adba6fd8797d836ce1957422b1b852b5cf1f2fbe2e56889de46f89acfb33c3f9",
  "cid": "QmV1adba6fd8797d836ce1957422b1b852b5cf1f2fbe",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288789,
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
      "evaluated_at": 1760288789
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
  "sig": "e54c914f09968249098965275b9549ad236f579fa5dcf999e85cdebc2d0963cd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271109324
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 104, 'threshold': 50, 'total_amount': 26000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 103, 'first_seen': 1760285764, 'matching_hash': '28f72b559ab32ea0'}}}