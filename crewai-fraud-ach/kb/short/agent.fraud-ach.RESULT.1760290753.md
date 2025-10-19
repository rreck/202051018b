```json
{
  "id": "52f19fdbc9901ee8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290753,
  "host_pid": "9e6742732c60:1",
  "hash": "54058c267c968d5be7fdbf18aaad5e8d23fed33a1e433bca08b09974265bd6b2",
  "cid": "QmV154058c267c968d5be7fdbf18aaad5e8d23fed33a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290753,
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
      "evaluated_at": 1760290753
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
  "sig": "59adbdc55e03f1f667db11f0f593a681b2b04200b6a6f25dd99a36a0461e6d96"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271167358
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 158, 'threshold': 50, 'total_amount': 66712814, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 157, 'first_seen': 1760285764, 'matching_hash': '04665d3443258f76'}}}