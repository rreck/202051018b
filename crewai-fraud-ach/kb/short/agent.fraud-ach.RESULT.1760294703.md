```json
{
  "id": "31457239d7f02e79",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294703,
  "host_pid": "9e6742732c60:1",
  "hash": "904a102201fdfe1e8ba82cb575ee07b4b6980880ee24e6751633e874bb5aebe8",
  "cid": "QmV1904a102201fdfe1e8ba82cb575ee07b4b6980880",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294703,
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
      "evaluated_at": 1760294703
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
  "sig": "aeaad969667da9573efda8b944ca5ccd5aeefff16095f3dcdda12081c1faa159"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026691588
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 98334081, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285763, 'matching_hash': '1da0382cf03ec7d2'}}}nd_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}