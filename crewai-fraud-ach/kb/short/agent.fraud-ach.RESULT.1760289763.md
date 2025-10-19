```json
{
  "id": "29d927e9644d5f1f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289763,
  "host_pid": "9e6742732c60:1",
  "hash": "dd8f8c575df3e22c2518f59dc00c90d3c8801a74b7900002e6f4d38f38afbf2f",
  "cid": "QmV1dd8f8c575df3e22c2518f59dc00c90d3c8801a74",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289763,
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
      "evaluated_at": 1760289763
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
  "sig": "55ee4bc9551477577c0e37c3a708751e9c34818a67db6006cdbdba9c9432a913"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469526930
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 132, 'threshold': 50, 'total_amount': 15018696, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 131, 'first_seen': 1760285764, 'matching_hash': 'b6b808f7611ea662'}}}