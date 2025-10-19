```json
{
  "id": "3e0ac54fd24b4da9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292620,
  "host_pid": "9e6742732c60:1",
  "hash": "92735d804b724dc492f5bb86c1e8c3e89fbae77efac16a253f3ed2a1e816e5d1",
  "cid": "QmV192735d804b724dc492f5bb86c1e8c3e89fbae77e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292620,
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
      "evaluated_at": 1760292620
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
  "sig": "727811f4d143e4041be1c7fe9e7767ae3da34c45eaa27bd6cad9b3818170aac0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038099532
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 201, 'threshold': 50, 'total_amount': 80685822, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 200, 'first_seen': 1760285765, 'matching_hash': 'ac68ba9e81a65c72'}}}