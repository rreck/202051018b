```json
{
  "id": "cc091c59680134f8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291458,
  "host_pid": "9e6742732c60:1",
  "hash": "377c0c1efb2e9513d49221178b781123b4d888f8b04431477daaac7aec11aeca",
  "cid": "QmV1377c0c1efb2e9513d49221178b781123b4d888f8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291458,
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
      "evaluated_at": 1760291458
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
  "sig": "2e312b03a09a62413ba971a91e841557cd80c77e4366211031fe57f2b8d3b5bb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152922139
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 175, 'threshold': 50, 'total_amount': 34995100, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 174, 'first_seen': 1760285765, 'matching_hash': '36c7f170a3aff02c'}}}