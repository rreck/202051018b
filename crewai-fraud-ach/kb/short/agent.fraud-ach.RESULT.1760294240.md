```json
{
  "id": "725b4ec3b2b325ff",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294240,
  "host_pid": "9e6742732c60:1",
  "hash": "9fade76f6b59e59304c01775cfbdcb3bedec99342b8f11746128b3c089e2fe40",
  "cid": "QmV19fade76f6b59e59304c01775cfbdcb3bedec9934",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294240,
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
      "evaluated_at": 1760294240
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
  "sig": "ec2d6556bf4ac5c65f810057907a655b0ece7981e10eff433feeb3c979f5f3ce"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021222877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 23400000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285765, 'matching_hash': 'c44c29fab5dec0d9'}}}