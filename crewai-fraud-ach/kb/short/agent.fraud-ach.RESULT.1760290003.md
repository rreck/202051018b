```json
{
  "id": "bd18bef8c6488870",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290003,
  "host_pid": "9e6742732c60:1",
  "hash": "ba4fdce1981f7e1bab2c1653cf575eb648cc13a38b74e81e427caa6bed981037",
  "cid": "QmV1ba4fdce1981f7e1bab2c1653cf575eb648cc13a3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290003,
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
      "evaluated_at": 1760290003
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
  "sig": "22c57d45d8fc548339e41da2d7ebcc6a4edebae256558ae38bf8d237d2e7f266"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000035614968
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 139, 'threshold': 50, 'total_amount': 43656008, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 138, 'first_seen': 1760285763, 'matching_hash': '3b03546121bd72f8'}}}