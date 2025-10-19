```json
{
  "id": "251930ea2b768506",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286666,
  "host_pid": "9e6742732c60:1",
  "hash": "10f0fc9cef8babf5f70e497c636c0e008c7d6a030149da05704026bf63491cb4",
  "cid": "QmV110f0fc9cef8babf5f70e497c636c0e008c7d6a03",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286666,
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
      "evaluated_at": 1760286666
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "c9b6312d8567e5f9dd5f2d47b8e8a02732df6940f8f173793570f145f500e1c1"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000247026993
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 14527689, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 32, 'first_seen': 1760285764, 'matching_hash': '7c7d13001f766fd7'}}}