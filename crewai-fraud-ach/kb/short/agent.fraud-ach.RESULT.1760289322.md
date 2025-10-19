```json
{
  "id": "de47fdf1b9147e65",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289322,
  "host_pid": "9e6742732c60:1",
  "hash": "d8c719145eb3c0702198c6d00b2cec8722f94b241515ec008ccee387579ed8ae",
  "cid": "QmV1d8c719145eb3c0702198c6d00b2cec8722f94b24",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289322,
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
      "evaluated_at": 1760289322
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
  "sig": "54ea59fc15494615fac36771898d15114452c36144f9cff26173cc394d8ddeb9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025087725
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 120, 'threshold': 50, 'total_amount': 45401640, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 119, 'first_seen': 1760285763, 'matching_hash': '6f7a0cdb6265bdfa'}}}