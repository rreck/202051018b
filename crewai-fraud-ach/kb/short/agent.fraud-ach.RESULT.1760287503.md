```json
{
  "id": "6903c1d373db97e1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287503,
  "host_pid": "9e6742732c60:1",
  "hash": "e2ddba97b143549f02e1f171877a9e83fa2dda84c73be9e5eb5965dfa4360e76",
  "cid": "QmV1e2ddba97b143549f02e1f171877a9e83fa2dda84",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287503,
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
      "evaluated_at": 1760287503
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
  "sig": "8ca7c22e30e84790c753548f21cd50a392ed11be44a06e3007eaa043c1e42138"
}
```

Fraud detected: duplicate_transaction (score: 79)
Transaction: 021000020143117
Details: {'velocity': {'fraud_detected': True, 'risk_score': 74, 'details': {'transaction_count': 62, 'threshold': 50, 'total_amount': 15500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 61, 'first_seen': 1760285765, 'matching_hash': '83c798d1c8d9cfec'}}}