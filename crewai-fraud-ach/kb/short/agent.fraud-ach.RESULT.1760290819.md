```json
{
  "id": "b8739bb87c5b0a89",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290819,
  "host_pid": "9e6742732c60:1",
  "hash": "321a7a8970bd36c107f83c13d376abb5c9d9ab17e2c7a74d398590ee0ad041a9",
  "cid": "QmV1321a7a8970bd36c107f83c13d376abb5c9d9ab17",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290819,
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
      "evaluated_at": 1760290819
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
  "sig": "9e95d7fb3765c57e99da4b6a5a422d27c35196aa2f7fda07fd0136ede19973e7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154787030
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 160, 'threshold': 50, 'total_amount': 70350400, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 159, 'first_seen': 1760285764, 'matching_hash': '945ae0d1ce138c7f'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}