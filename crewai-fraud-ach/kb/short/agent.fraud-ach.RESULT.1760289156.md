```json
{
  "id": "258f57048f029b28",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289156,
  "host_pid": "9e6742732c60:1",
  "hash": "6f5588452b89c996dbcec28d941362c3845d35c5fe7920c7bbec72ee4d423324",
  "cid": "QmV16f5588452b89c996dbcec28d941362c3845d35c5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289156,
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
      "evaluated_at": 1760289156
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
  "sig": "e1668c8688ec0553ea57fdea7d4c29d1c2df064bd9a5a13aa3a87dc8f1dec339"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469615703
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 115, 'threshold': 50, 'total_amount': 21908305, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 114, 'first_seen': 1760285763, 'matching_hash': '33adc30ff3203421'}}}