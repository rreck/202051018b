```json
{
  "id": "72a5d1006c6b958c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290049,
  "host_pid": "9e6742732c60:1",
  "hash": "ccdf459a12a07da9c6140a5941fd0c62fff99bfdbe41f55081b163baf51fb158",
  "cid": "QmV1ccdf459a12a07da9c6140a5941fd0c62fff99bfd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290049,
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
      "evaluated_at": 1760290049
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
  "sig": "157ca794c14600235dd84ed2de0644ffe983c9e32ba42e11dd69b9cee88f895c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592568865
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 140, 'threshold': 50, 'total_amount': 33877480, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 139, 'first_seen': 1760285763, 'matching_hash': 'ecded74c6845c7bc'}}}