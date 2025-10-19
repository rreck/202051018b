```json
{
  "id": "45c7b740692a349e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288394,
  "host_pid": "9e6742732c60:1",
  "hash": "27d22ad20a4bd05b8e5ad52b0d3e911f52d490d006167ad92c829f29149eaa9d",
  "cid": "QmV127d22ad20a4bd05b8e5ad52b0d3e911f52d490d0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288394,
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
      "evaluated_at": 1760288394
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
  "sig": "ba41e323e923c7d4c4578a9f801cdf01e02e4cf62f5f5eec4b6dc967f182023d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023603818
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 92, 'threshold': 50, 'total_amount': 41310392, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 91, 'first_seen': 1760285764, 'matching_hash': '07334b550f79eb68'}}}