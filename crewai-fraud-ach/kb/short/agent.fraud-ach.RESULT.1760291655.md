```json
{
  "id": "346166eb410e7a12",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291655,
  "host_pid": "9e6742732c60:1",
  "hash": "6f02ae0d0e69b56de1bae5ce74b29693bd023dce05e242ed0fb85ea74cda306a",
  "cid": "QmV16f02ae0d0e69b56de1bae5ce74b29693bd023dce",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291655,
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
      "evaluated_at": 1760291655
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
  "sig": "2a79d70a0740c79e9540c5fa52371c952a90b322d193535a9b0fbee450a3c5bd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021861158
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 180, 'threshold': 50, 'total_amount': 46119240, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 179, 'first_seen': 1760285763, 'matching_hash': '4f96dd6d0eca8862'}}}