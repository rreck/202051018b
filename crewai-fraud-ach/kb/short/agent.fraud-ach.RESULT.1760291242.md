```json
{
  "id": "942e2d30337af25f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291242,
  "host_pid": "9e6742732c60:1",
  "hash": "d794b42e5740abbe28ba7c187f6e8a96d0cd8ff713f33c794321b788623da88b",
  "cid": "QmV1d794b42e5740abbe28ba7c187f6e8a96d0cd8ff7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291242,
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
      "evaluated_at": 1760291242
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
  "sig": "218ffad63bc9a474fb9b2b1c42898a7f1466bdb1a765f0f4fc8679ed8102e973"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024765233
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 170, 'threshold': 50, 'total_amount': 57979860, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 169, 'first_seen': 1760285763, 'matching_hash': 'feb1cc4bc40c71bc'}}}