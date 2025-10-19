```json
{
  "id": "9e23b063888cfa57",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291820,
  "host_pid": "9e6742732c60:1",
  "hash": "4bf97a2a4ca10c703a5c596b0542456f284b7c936eded77a6e4a7b3d8437f472",
  "cid": "QmV14bf97a2a4ca10c703a5c596b0542456f284b7c93",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291820,
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
      "evaluated_at": 1760291820
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
  "sig": "e65a1004d8d1b315e9a2007d86a9de9670871c88db77477eb2860d3a4ff7a9bd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467455813
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 184, 'threshold': 50, 'total_amount': 12480720, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 183, 'first_seen': 1760285763, 'matching_hash': 'dd25b8ab6718ff18'}}}