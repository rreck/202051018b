```json
{
  "id": "aaf25534180c1cba",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292510,
  "host_pid": "9e6742732c60:1",
  "hash": "171168437c15c6d905669a2f2cc448904a14ac7f67d27d017ec527466852b1ab",
  "cid": "QmV1171168437c15c6d905669a2f2cc448904a14ac7f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292510,
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
      "evaluated_at": 1760292510
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
  "sig": "2c3048bfd7965a8dfb4303a5002e2b146969777873e8fab742b814f3149020c9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024421000
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 199, 'threshold': 50, 'total_amount': 90010685, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 198, 'first_seen': 1760285763, 'matching_hash': 'ab9abea401ffdb4a'}}}