```json
{
  "id": "1bf89822ff944241",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292453,
  "host_pid": "9e6742732c60:1",
  "hash": "99b6782d73d4b081e1fb6fccd0cf7c088c68e70820ff2704c6541533f1bc2732",
  "cid": "QmV199b6782d73d4b081e1fb6fccd0cf7c088c68e708",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292453,
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
      "evaluated_at": 1760292453
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
  "sig": "c63baaec0ad078ebedfa3fe3f2287508a76f8399def9d48eb66cde71f2f27787"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241647784
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 198, 'threshold': 50, 'total_amount': 21766932, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 197, 'first_seen': 1760285763, 'matching_hash': '5747783cddc76b25'}}}