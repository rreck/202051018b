```json
{
  "id": "7600a85458472f34",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290445,
  "host_pid": "9e6742732c60:1",
  "hash": "82dc1e7f386d8bba43f9e2e566ef61c9d3500b85a0a05811674ca6b58e0f3c62",
  "cid": "QmV182dc1e7f386d8bba43f9e2e566ef61c9d3500b85",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290445,
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
      "evaluated_at": 1760290445
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
  "sig": "22a3598e114bd1130dc25bd257bd25f37e71ff9725add1b7e34df927ce93d8d3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039867307
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 150, 'threshold': 50, 'total_amount': 10276350, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 149, 'first_seen': 1760285765, 'matching_hash': '2a6987d2199b8b86'}}}