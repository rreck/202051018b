```json
{
  "id": "a56a3636adad918b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287439,
  "host_pid": "9e6742732c60:1",
  "hash": "f4c291cd641ca6781a7c8ba11602c4ce433d5f3ffcebcc66656441b36000b88a",
  "cid": "QmV1f4c291cd641ca6781a7c8ba11602c4ce433d5f3f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287439,
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
      "evaluated_at": 1760287439
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
  "sig": "e939154ae467cb73580bafa0928bb8f82999d662135a41f3cf75773be58a7dcc"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000024023598
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 60, 'threshold': 50, 'total_amount': 16098000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 59, 'first_seen': 1760285763, 'matching_hash': 'b47dddaceabbc6a8'}}}