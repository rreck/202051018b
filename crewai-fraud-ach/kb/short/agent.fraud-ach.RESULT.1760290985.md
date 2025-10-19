```json
{
  "id": "72eff8bf5ebbf6f9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290985,
  "host_pid": "9e6742732c60:1",
  "hash": "d53e4cc73aea857aaa2c546ab787a8ad0af606c31f3ada8c1c83b06deb72c889",
  "cid": "QmV1d53e4cc73aea857aaa2c546ab787a8ad0af606c3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290985,
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
      "evaluated_at": 1760290985
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
  "sig": "61b298628d1e37a9f4c7ee2e78b75c79a1a30715f8ac584025253f976e126ff4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276997857
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 164, 'threshold': 50, 'total_amount': 78022508, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 163, 'first_seen': 1760285763, 'matching_hash': 'b73e9a6de72cc131'}}}