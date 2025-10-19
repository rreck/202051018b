```json
{
  "id": "7e9fd8e6d609ed00",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291750,
  "host_pid": "9e6742732c60:1",
  "hash": "e4b0d9a35b742e8552e6a52509391c16f29056de7f9ab2392e8f5265219250e3",
  "cid": "QmV1e4b0d9a35b742e8552e6a52509391c16f29056de",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291750,
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
      "evaluated_at": 1760291750
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
  "sig": "bbe302eeea363959d919135d7494614b925b8f6232ed8b8be15a48dc4412a777"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596082668
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 258, 'threshold': 50, 'total_amount': 55487802, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 257, 'first_seen': 1760284979, 'matching_hash': '3a96bbca6babd2b6'}}}