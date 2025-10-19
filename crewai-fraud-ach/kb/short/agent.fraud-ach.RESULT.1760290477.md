```json
{
  "id": "5b8084ce9072c479",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290477,
  "host_pid": "9e6742732c60:1",
  "hash": "df962f1a8a08c08548662baad65d94fe5e8dd13adceb35137b167412805f679b",
  "cid": "QmV1df962f1a8a08c08548662baad65d94fe5e8dd13a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290477,
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
      "evaluated_at": 1760290477
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
  "sig": "a80ef8dfe081d6613577e68db964ba9ae4418deaaad1d0e29993fd54cd660a08"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460191060
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 151, 'threshold': 50, 'total_amount': 52622896, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 150, 'first_seen': 1760285764, 'matching_hash': '1d882c6abf3447ef'}}}