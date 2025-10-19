```json
{
  "id": "8d6b85dea7f6e4af",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293359,
  "host_pid": "9e6742732c60:1",
  "hash": "4f99398a1e2b4298d4aa3431a0417202df960d22d98e23f0040c13f10a51634b",
  "cid": "QmV14f99398a1e2b4298d4aa3431a0417202df960d22",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293359,
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
      "evaluated_at": 1760293359
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
  "sig": "834341b19784d896c81683cf36d39ba7d0d8a0c719f6c1ec3319d20efeda760a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038495907
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 217, 'threshold': 50, 'total_amount': 59024434, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 216, 'first_seen': 1760285763, 'matching_hash': '3a0df0e30691ba23'}}}