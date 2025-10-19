```json
{
  "id": "8f31d67686e4d4b5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293620,
  "host_pid": "9e6742732c60:1",
  "hash": "b3937c9fe37ff19c47e68ab7ab124bca310363d17b5c078acf2983ad8f6bfdb1",
  "cid": "QmV1b3937c9fe37ff19c47e68ab7ab124bca310363d1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293620,
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
      "evaluated_at": 1760293620
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
  "sig": "a2019b0f302be20bb995080901e312f2120cc0fdc0fbff2380b444d820188897"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276997857
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 222, 'threshold': 50, 'total_amount': 105615834, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 221, 'first_seen': 1760285763, 'matching_hash': 'b73e9a6de72cc131'}}}