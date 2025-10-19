```json
{
  "id": "590f348b7d23804e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288760,
  "host_pid": "9e6742732c60:1",
  "hash": "103b0a188cb3860420d07fab1b0de022ea8a0b4aa3042b7e863ed2e57d2ea5f1",
  "cid": "QmV1103b0a188cb3860420d07fab1b0de022ea8a0b4a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288760,
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
      "evaluated_at": 1760288760
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
  "sig": "e7c933bc13cbedb4b3d886b5b21653f587dd43a8a8c6635581681035e647e78f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021328085
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 179, 'threshold': 50, 'total_amount': 12365857, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 178, 'first_seen': 1760284979, 'matching_hash': 'f7c67db4baca4bf3'}}}