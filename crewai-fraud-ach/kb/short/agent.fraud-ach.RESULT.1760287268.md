```json
{
  "id": "f97355400a05583e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287268,
  "host_pid": "9e6742732c60:1",
  "hash": "a2b13540e47ce84f2e5541b834b8897fbb3b55dd39f0592072d30f7c9664c22a",
  "cid": "QmV1a2b13540e47ce84f2e5541b834b8897fbb3b55dd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287268,
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
      "evaluated_at": 1760287268
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
  "sig": "8664efbb6e90bd4db19742bd9132f7f08caa9f4b127550333365ff8379f3d096"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201460612944
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 54, 'threshold': 50, 'total_amount': 17764812, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 53, 'first_seen': 1760285763, 'matching_hash': 'ecd204bdadc44322'}}}