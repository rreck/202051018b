```json
{
  "id": "3d12d09e648f8a6a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291851,
  "host_pid": "9e6742732c60:1",
  "hash": "4c9f467fe4a1ceb82bf277da2bb2e27f9cf5550b902a9de6bd3f0b7f81463f96",
  "cid": "QmV14c9f467fe4a1ceb82bf277da2bb2e27f9cf5550b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291851,
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
      "evaluated_at": 1760291851
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
  "sig": "989cf1fdf5f855c9aa768ec1fb6f84a1f7b3b931c8d49b941214796fe3649174"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462765128
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 184, 'threshold': 50, 'total_amount': 55493112, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 183, 'first_seen': 1760285765, 'matching_hash': 'e332841741f2145e'}}}