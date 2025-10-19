```json
{
  "id": "f9070bddc0475a9e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289709,
  "host_pid": "9e6742732c60:1",
  "hash": "0831d0893cae30516d52aaf8b2c2c2e8a6aea6a2eaa418d9f3a6f18f0d8240ee",
  "cid": "QmV10831d0893cae30516d52aaf8b2c2c2e8a6aea6a2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289709,
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
      "evaluated_at": 1760289709
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
  "sig": "25444ffd474dc1e5b971d735c0ead6c79ac52248f6eabe50fb9b395c828d3c98"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000036798243
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 131, 'threshold': 50, 'total_amount': 57914052, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 130, 'first_seen': 1760285763, 'matching_hash': '9f3869b775bbb8aa'}}}