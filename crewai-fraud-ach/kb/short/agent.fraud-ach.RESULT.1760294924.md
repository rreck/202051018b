```json
{
  "id": "0ec6db64f01fb959",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294924,
  "host_pid": "9e6742732c60:1",
  "hash": "0d84ff22cb765fbe646a476684f08323ccd162534c122a55c8cecba5032af43d",
  "cid": "QmV10d84ff22cb765fbe646a476684f08323ccd16253",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294924,
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
      "evaluated_at": 1760294924
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
  "sig": "17dcc858daecf44525485b8183dbd3855884d793a2b5af648a50bcea819775e2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033386526
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 247, 'threshold': 50, 'total_amount': 35925656, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 246, 'first_seen': 1760285764, 'matching_hash': 'a3ad727f5ed38962'}}}