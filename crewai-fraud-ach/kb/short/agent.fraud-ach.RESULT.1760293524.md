```json
{
  "id": "8c41a4f5d5c0e615",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293524,
  "host_pid": "9e6742732c60:1",
  "hash": "0a03e79d750ea8dbf325a0c3b5f09c433b35b3a1a37fdb1ed17881420a1a0cfe",
  "cid": "QmV10a03e79d750ea8dbf325a0c3b5f09c433b35b3a1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293524,
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
      "evaluated_at": 1760293524
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
  "sig": "2e785e8a8847b219e4672e54b62fbbc7a48ffeb958fa8524183d795ebfeb0fed"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466150314
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 296, 'threshold': 50, 'total_amount': 83308608, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 295, 'first_seen': 1760284979, 'matching_hash': '93cc3488fa8b8da9'}}}