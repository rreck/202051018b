```json
{
  "id": "6bb38aec387c5ce7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293991,
  "host_pid": "9e6742732c60:1",
  "hash": "29e3851810ab05818c7865c57a813a30790131b5deda655f28d32f5e3b0707c9",
  "cid": "QmV129e3851810ab05818c7865c57a813a30790131b5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293991,
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
      "evaluated_at": 1760293991
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
  "sig": "310383937c413d486c0ca67c84ac8b2efed2f49c610877294579aec2f6e00ed7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032712851
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 19047304, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760285765, 'matching_hash': 'f72222764ca627d0'}}}