```json
{
  "id": "27bb454b5d0de7b2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289259,
  "host_pid": "9e6742732c60:1",
  "hash": "1f9811714c9be9e50d0fb888d0f8df498b3cd346274f200965a31eb4a0c64065",
  "cid": "QmV11f9811714c9be9e50d0fb888d0f8df498b3cd346",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289259,
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
      "evaluated_at": 1760289259
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
  "sig": "02633a41ecdbc2ba63e6218e8838998e65a292ca3a9d6eaa5a8d2e58ce58962c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464866805
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 118, 'threshold': 50, 'total_amount': 45505402, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 117, 'first_seen': 1760285764, 'matching_hash': '8f846e2074b125b7'}}}