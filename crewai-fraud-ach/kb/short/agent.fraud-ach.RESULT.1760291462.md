```json
{
  "id": "38eae488857fe3c0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291462,
  "host_pid": "9e6742732c60:1",
  "hash": "4951f7ff9ac7e3d4b5b86d1f1f8412e7fe238e793ef0623661029c1ab8f7452d",
  "cid": "QmV14951f7ff9ac7e3d4b5b86d1f1f8412e7fe238e79",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291462,
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
      "evaluated_at": 1760291462
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
  "sig": "0d84455fa8593c04c8c0f04e7d0b86bfc19173a8f209844cc464aad243cd4d57"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025001530
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 175, 'threshold': 50, 'total_amount': 42254450, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 174, 'first_seen': 1760285765, 'matching_hash': 'c7ad70870577ca51'}}}