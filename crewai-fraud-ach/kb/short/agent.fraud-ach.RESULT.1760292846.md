```json
{
  "id": "7ad93658455820f1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292846,
  "host_pid": "9e6742732c60:1",
  "hash": "b39c15d1474225ca16c43799292a3e8574f5bb4221797810873b44076afc667e",
  "cid": "QmV1b39c15d1474225ca16c43799292a3e8574f5bb42",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292846,
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
      "evaluated_at": 1760292846
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
  "sig": "6a801a02a71893c304b795b48220adce3e7663fcee2850f3600627b2f5e46a65"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000035025346
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 206, 'threshold': 50, 'total_amount': 33130774, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 205, 'first_seen': 1760285763, 'matching_hash': 'a8a877b5861d69af'}}}