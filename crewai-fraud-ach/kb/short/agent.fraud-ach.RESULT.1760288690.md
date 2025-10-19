```json
{
  "id": "16aabb1dd60593b8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288690,
  "host_pid": "9e6742732c60:1",
  "hash": "7d1df029c458096737425af4713280df5bbc9a6b01a534eaa0fcb43c3b5e42f3",
  "cid": "QmV17d1df029c458096737425af4713280df5bbc9a6b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288690,
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
      "evaluated_at": 1760288690
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
  "sig": "9676b614a0e4441bc83377098e116781c6360a7f8b0ac9bb30b0ef44ad9d3115"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596556765
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 101, 'threshold': 50, 'total_amount': 18548044, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 100, 'first_seen': 1760285763, 'matching_hash': '746e82f5d57aeb25'}}}