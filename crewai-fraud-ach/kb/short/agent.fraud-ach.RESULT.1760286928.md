```json
{
  "id": "dc57d46ecdfc6d68",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286928,
  "host_pid": "9e6742732c60:1",
  "hash": "095a79a8ad4bf87c9c3f8c45c8bdee1c60c61e047dab8e21b8f7818d83225bf5",
  "cid": "QmV1095a79a8ad4bf87c9c3f8c45c8bdee1c60c61e04",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286928,
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
      "evaluated_at": 1760286928
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
  "sig": "72105fd6a9a937f93b503ca0415a27711938235e7646b226fd9c1f09eb34002f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596082668
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 118, 'threshold': 50, 'total_amount': 25378142, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 117, 'first_seen': 1760284979, 'matching_hash': '3a96bbca6babd2b6'}}}