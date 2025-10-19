```json
{
  "id": "3e37725ffe340f69",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288993,
  "host_pid": "9e6742732c60:1",
  "hash": "d88d457ad4a3a38529de3c400766613c255a31c600a7656f8e56d72507c00a1b",
  "cid": "QmV1d88d457ad4a3a38529de3c400766613c255a31c6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288993,
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
      "evaluated_at": 1760288993
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
  "sig": "a5e3ac2641cc4bedfbaa412d3d1002069dba9734bf82a65228ef19cd4ea3f5c3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029163318
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 110, 'threshold': 50, 'total_amount': 33930270, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 109, 'first_seen': 1760285765, 'matching_hash': 'b5567c8565e47211'}}}