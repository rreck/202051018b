```json
{
  "id": "e2609b7ee6b84830",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286550,
  "host_pid": "9e6742732c60:1",
  "hash": "a18d3c380645ce9d8603cf106c1818af6f85bb610172816dcc919ee246ce74a4",
  "cid": "QmV1a18d3c380645ce9d8603cf106c1818af6f85bb61",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286550,
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
      "evaluated_at": 1760286550
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
  "sig": "31736dc1aa20d1ed5c3f30bb3548f6867762acf320d15e55c9794de848e274df"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009596363200
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11069822, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 28, 'first_seen': 1760285764, 'matching_hash': 'b9f8fedd6c477a32'}}}