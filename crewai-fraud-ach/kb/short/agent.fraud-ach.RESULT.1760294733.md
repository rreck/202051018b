```json
{
  "id": "73cfa78963fbf033",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294733,
  "host_pid": "9e6742732c60:1",
  "hash": "85c17518477551f32958f63afccf549bd94d52d2fc906809c25942b2a1f85902",
  "cid": "QmV185c17518477551f32958f63afccf549bd94d52d2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294733,
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
      "evaluated_at": 1760294733
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
  "sig": "d1cabd302bcddf540a7cd8a8e313068a9ae18c06bce1523da5eda031f1fb48a9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032712851
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 20211768, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285765, 'matching_hash': 'f72222764ca627d0'}}}