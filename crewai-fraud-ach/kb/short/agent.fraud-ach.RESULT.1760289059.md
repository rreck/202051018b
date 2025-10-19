```json
{
  "id": "f773ca94e87b6401",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289059,
  "host_pid": "9e6742732c60:1",
  "hash": "982b3e7fc479e11880b90226be2dca108fd0f4b0252f6616d27bbbb039d39cfb",
  "cid": "QmV1982b3e7fc479e11880b90226be2dca108fd0f4b0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289059,
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
      "evaluated_at": 1760289059
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
  "sig": "2a0364c2c94ea978df912646c291eafa779f1b8748a9ffeac1bfc0c86ec47951"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245928241
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 112, 'threshold': 50, 'total_amount': 38297952, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 111, 'first_seen': 1760285763, 'matching_hash': '062a48cd408462a2'}}}aly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 5062727}}}