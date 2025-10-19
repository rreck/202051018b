```json
{
  "id": "2da555865935d07d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294920,
  "host_pid": "9e6742732c60:1",
  "hash": "1a2eb31c5d30b93ed7940d7048046375f60347ea089cfc77686949684b64e965",
  "cid": "QmV11a2eb31c5d30b93ed7940d7048046375f60347ea",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294920,
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
      "evaluated_at": 1760294920
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
  "sig": "e824c1aa07defa90d2d9ff163d3fed891b99f2eef06e9ee223cf217246a0abf2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154405665
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 247, 'threshold': 50, 'total_amount': 119052518, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 246, 'first_seen': 1760285763, 'matching_hash': '36d51f87c7d176f1'}}}