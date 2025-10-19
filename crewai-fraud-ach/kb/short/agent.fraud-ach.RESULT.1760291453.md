```json
{
  "id": "d3dcf3d36bc43d54",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291453,
  "host_pid": "9e6742732c60:1",
  "hash": "d174ea637fdace0578a28d93310c01cc0fdb449de67eaf91aa2791c72d07ff28",
  "cid": "QmV1d174ea637fdace0578a28d93310c01cc0fdb449d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291453,
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
      "evaluated_at": 1760291453
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
  "sig": "31b78478922de066ed362046e52f8bffa21cb43627fb82b851eeff37e5fe1327"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029313979
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 175, 'threshold': 50, 'total_amount': 82709725, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 174, 'first_seen': 1760285765, 'matching_hash': 'ee97e2abac1557d2'}}}