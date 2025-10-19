```json
{
  "id": "346c39cda73251a9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292940,
  "host_pid": "9e6742732c60:1",
  "hash": "0cc29862d5fb639f1a140deebeaf385d9aab852b850ce67d4064c79a58d1d598",
  "cid": "QmV10cc29862d5fb639f1a140deebeaf385d9aab852b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292940,
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
      "evaluated_at": 1760292940
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
  "sig": "aa1a6c7a02e10d23c6341d89de780d3beb5000ceea71b470e59d928397740d4f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596082668
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 284, 'threshold': 50, 'total_amount': 61079596, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 283, 'first_seen': 1760284979, 'matching_hash': '3a96bbca6babd2b6'}}}