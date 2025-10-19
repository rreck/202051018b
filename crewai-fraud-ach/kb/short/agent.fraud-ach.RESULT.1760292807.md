```json
{
  "id": "905067687c79f3cb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292807,
  "host_pid": "9e6742732c60:1",
  "hash": "60163356416f706369348961bcb3407f3d57c38ca4e6a28ed6474b3401d2ce28",
  "cid": "QmV160163356416f706369348961bcb3407f3d57c38c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292807,
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
      "evaluated_at": 1760292807
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
  "sig": "08378ba641b62ae1da3720d15c04012bdab474272426553203cd7646ca4dcb58"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100273461392
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 205, 'threshold': 50, 'total_amount': 73121860, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 204, 'first_seen': 1760285765, 'matching_hash': 'ee78248c8d3d65fe'}}}