```json
{
  "id": "360ce9085245c018",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292187,
  "host_pid": "9e6742732c60:1",
  "hash": "5aba4477c3efaef8c0f818e80b7ff9ed2a3eaf32e33d1daaea33e11e87942fe5",
  "cid": "QmV15aba4477c3efaef8c0f818e80b7ff9ed2a3eaf32",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292187,
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
      "evaluated_at": 1760292187
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
  "sig": "ab3307daeb7d26eeb49690bf990e070fd1890bf0b12396bf815ff33d5010c19f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021479776
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 192, 'threshold': 50, 'total_amount': 44262912, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 191, 'first_seen': 1760285763, 'matching_hash': '6c002fd60c3e5dde'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '051442869', 'validation_error': 'Invalid routing number checksum'}}}