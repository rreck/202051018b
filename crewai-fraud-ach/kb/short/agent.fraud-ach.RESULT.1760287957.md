```json
{
  "id": "a1fe802538f51335",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287957,
  "host_pid": "9e6742732c60:1",
  "hash": "d8454c4f44156e550aca0d634b18f13b86f9ebe234684a739046acc07908e8a0",
  "cid": "QmV1d8454c4f44156e550aca0d634b18f13b86f9ebe2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287957,
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
      "evaluated_at": 1760287957
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
  "sig": "d7b23f5194c76c1a9f150ab27b6a74684d0aad659aceced6d73147bdc1eb52e5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592648645
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 78, 'threshold': 50, 'total_amount': 29500146, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 77, 'first_seen': 1760285763, 'matching_hash': 'd7971b176fb0516b'}}}