```json
{
  "id": "a156ad94284ed657",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294791,
  "host_pid": "9e6742732c60:1",
  "hash": "5f3aa4e1ca980010906d7fada0c6ac9fef9122c7dddfa7ec80dc08a9ad52daaa",
  "cid": "QmV15f3aa4e1ca980010906d7fada0c6ac9fef9122c7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294791,
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
      "evaluated_at": 1760294791
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
  "sig": "eab9c80737e24f49e4bff5175fc1f428d9e00ee50476135519bedbde30e82078"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033965137
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 34813920, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285765, 'matching_hash': 'a94abbf708458614'}}}