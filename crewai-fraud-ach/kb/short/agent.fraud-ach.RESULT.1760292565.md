```json
{
  "id": "ec80883b6df05ee3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292565,
  "host_pid": "9e6742732c60:1",
  "hash": "a9038c995e8c48a854bcf16d1d4799ab2a44a95907adf1c47889382cbe7e626b",
  "cid": "QmV1a9038c995e8c48a854bcf16d1d4799ab2a44a959",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292565,
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
      "evaluated_at": 1760292565
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
  "sig": "5590644be9efa3655b743f7be2f7c4d143c9480a0e74cb6e31e9aab0388f57d8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034053694
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 200, 'threshold': 50, 'total_amount': 10720400, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 199, 'first_seen': 1760285765, 'matching_hash': 'f3f5d61420936f73'}}}nd_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}