```json
{
  "id": "d93f7230b97b1562",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290957,
  "host_pid": "9e6742732c60:1",
  "hash": "5308994ca2cae3b011277b154bc539365bb1ded8ede791c0d82e95a67fcc984e",
  "cid": "QmV15308994ca2cae3b011277b154bc539365bb1ded8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290957,
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
      "evaluated_at": 1760290957
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
  "sig": "2694ac87beed2e9ffc60f88cede81c736898e45a7ae5d9c0e54b299868dd17ed"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025341515
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 163, 'threshold': 50, 'total_amount': 40952772, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 162, 'first_seen': 1760285765, 'matching_hash': '76c6a410184ad94b'}}}