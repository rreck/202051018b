```json
{
  "id": "da40b377a29a1f8d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291531,
  "host_pid": "9e6742732c60:1",
  "hash": "8cecc5fc84ce17de62dc05fbffed0d9128a112cdf07af67152fdb4b46a053745",
  "cid": "QmV18cecc5fc84ce17de62dc05fbffed0d9128a112cd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291531,
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
      "evaluated_at": 1760291531
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
  "sig": "7501c7a6eba5050cb4aebad4a772b1bd753811f72b292b5562d40f176331370e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465124688
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 177, 'threshold': 50, 'total_amount': 29125881, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 176, 'first_seen': 1760285763, 'matching_hash': 'c4099eb9aeb13a11'}}}