```json
{
  "id": "f40e41eec2fb8bbe",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288716,
  "host_pid": "9e6742732c60:1",
  "hash": "45e6704041e73bb726214d43a73a4bdb774b4a41cbd2aa651737c721047888be",
  "cid": "QmV145e6704041e73bb726214d43a73a4bdb774b4a41",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288716,
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
      "evaluated_at": 1760288716
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
  "sig": "9548758bc234c70654831fe9deb5c53e99ecd0fb751b2ccd295c4d6b43bc1847"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105159149641
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 102, 'threshold': 50, 'total_amount': 19752912, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 101, 'first_seen': 1760285763, 'matching_hash': '1bdba49a970d4caa'}}}