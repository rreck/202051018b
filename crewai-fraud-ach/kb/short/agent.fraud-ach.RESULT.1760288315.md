```json
{
  "id": "61dd4aa0e8a8eeca",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288315,
  "host_pid": "9e6742732c60:1",
  "hash": "ff3fbe7e3e41a94829ba8afe0273ec9f8ebec0dc26bb4fdaf23373a88837845a",
  "cid": "QmV1ff3fbe7e3e41a94829ba8afe0273ec9f8ebec0dc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288315,
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
      "evaluated_at": 1760288315
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
  "sig": "e3ce0471f6120c465f731fff025163a6982c930e2d3ed4ac2b78d4330e1c1198"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022243877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 89, 'threshold': 50, 'total_amount': 22250000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 88, 'first_seen': 1760285765, 'matching_hash': '9c2417d6ee361cba'}}}