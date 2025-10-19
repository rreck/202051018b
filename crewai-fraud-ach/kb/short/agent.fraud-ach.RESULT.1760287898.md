```json
{
  "id": "5859e9aba34f9082",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287898,
  "host_pid": "9e6742732c60:1",
  "hash": "aeb2c6e7c10e2ada393a5878d50c25467f84e3f89e611709d04f8101ddfd118f",
  "cid": "QmV1aeb2c6e7c10e2ada393a5878d50c25467f84e3f8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287898,
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
      "evaluated_at": 1760287898
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
  "sig": "4a2324946312a398f38136bbf9dd55cfed742cd72350572b4d4ae5304f740312"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241906665
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 76, 'threshold': 50, 'total_amount': 19699048, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 75, 'first_seen': 1760285764, 'matching_hash': '6ca698820fae5f27'}}}