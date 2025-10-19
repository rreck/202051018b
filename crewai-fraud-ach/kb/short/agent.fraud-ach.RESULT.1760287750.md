```json
{
  "id": "8e801292e47dc5db",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287750,
  "host_pid": "9e6742732c60:1",
  "hash": "9d18b6276e65416c5d296e3c8bb06d82d5bc2553b718218cea7d0ef66715941e",
  "cid": "QmV19d18b6276e65416c5d296e3c8bb06d82d5bc2553",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287750,
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
      "evaluated_at": 1760287750
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
  "sig": "a7a6f6a9f170903aaeca140ec1505aab4089844b171f34b28e8153c0723ee9e9"
}
```

Fraud detected: duplicate_transaction (score: 88)
Transaction: 026009596556765
Details: {'velocity': {'fraud_detected': True, 'risk_score': 92, 'details': {'transaction_count': 71, 'threshold': 50, 'total_amount': 13038724, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 70, 'first_seen': 1760285763, 'matching_hash': '746e82f5d57aeb25'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}