```json
{
  "id": "3ed0455ceb0b44bd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294030,
  "host_pid": "9e6742732c60:1",
  "hash": "ae9c432cde34aefb15c7e0fe2ad0a5ff86611ead9acd4b94561ddf627854160e",
  "cid": "QmV1ae9c432cde34aefb15c7e0fe2ad0a5ff86611ead",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294030,
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
      "evaluated_at": 1760294030
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
  "sig": "28c564dd7e55f20c0760cc3afbfa6e0c14f14cd4b60746a8fb510f3a6e93f15f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596082668
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 306, 'threshold': 50, 'total_amount': 65811114, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 305, 'first_seen': 1760284979, 'matching_hash': '3a96bbca6babd2b6'}}}