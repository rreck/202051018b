```json
{
  "id": "e6ddacd6787a7a6a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293935,
  "host_pid": "9e6742732c60:1",
  "hash": "fee9b0fcbd7146b4b9c87b46fade19bf15ed14631538719b63daacdd64b25636",
  "cid": "QmV1fee9b0fcbd7146b4b9c87b46fade19bf15ed1463",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293935,
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
      "evaluated_at": 1760293935
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
  "sig": "d53e5b11d90c1c02e4938cf6da9d35b607d95517a89acdb5f933499842b973c6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156760115
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 228, 'threshold': 50, 'total_amount': 73136016, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 227, 'first_seen': 1760285764, 'matching_hash': '84a7174d04c2e814'}}}