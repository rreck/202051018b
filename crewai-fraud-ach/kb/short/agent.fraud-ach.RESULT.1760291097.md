```json
{
  "id": "a45f6f8d86b5adab",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291097,
  "host_pid": "9e6742732c60:1",
  "hash": "46ac0ad804e0a12527e86e5ee82f41a39db0ecf88dc8b50b7f288965d63f5988",
  "cid": "QmV146ac0ad804e0a12527e86e5ee82f41a39db0ecf8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291097,
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
      "evaluated_at": 1760291097
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
  "sig": "0c8eaf4584e5b7249a3b628d11c1c9e3e47f4080d1b1e5ef223ec31d0acdade2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593506815
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 167, 'threshold': 50, 'total_amount': 70048985, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 166, 'first_seen': 1760285763, 'matching_hash': '152f3a2a027ae633'}}}