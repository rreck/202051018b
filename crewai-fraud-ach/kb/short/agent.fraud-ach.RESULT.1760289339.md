```json
{
  "id": "78f6118a76ddce9b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289339,
  "host_pid": "9e6742732c60:1",
  "hash": "5c5344fead37433ee05c29f9f73f34a36179f02ff1e7db2d45aa91836267de04",
  "cid": "QmV15c5344fead37433ee05c29f9f73f34a36179f02f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289339,
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
      "evaluated_at": 1760289339
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
  "sig": "3ec2ed1617b0aedcd36b80e33042ab8b5da74f054b1588f2514d85659f64a4a1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000024109289
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 120, 'threshold': 50, 'total_amount': 41924280, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 119, 'first_seen': 1760285765, 'matching_hash': 'ac2c8f9ff893d8ff'}}}