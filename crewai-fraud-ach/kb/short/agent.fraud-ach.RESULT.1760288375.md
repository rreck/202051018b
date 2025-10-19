```json
{
  "id": "1e55b75146d552b3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288375,
  "host_pid": "9e6742732c60:1",
  "hash": "11a184202a1bfe5ff5cc2afeb67c9b708bf74f0580e5c574905b3a9fb04e6c79",
  "cid": "QmV111a184202a1bfe5ff5cc2afeb67c9b708bf74f05",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288375,
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
      "evaluated_at": 1760288375
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
  "sig": "64eb48139e5f2e36e1bd5003abeae04b35a0e401ae449698ebf6a99908d43cc7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029832912
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 91, 'threshold': 50, 'total_amount': 41749799, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 90, 'first_seen': 1760285765, 'matching_hash': 'ede6214022caf300'}}}