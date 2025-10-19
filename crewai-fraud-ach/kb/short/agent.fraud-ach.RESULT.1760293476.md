```json
{
  "id": "42036c9816b0daf8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293476,
  "host_pid": "9e6742732c60:1",
  "hash": "9bdc4ff3033d705c88bbcf0ea060568fdc20ca375fee5ef46bcfc49cad13a94c",
  "cid": "QmV19bdc4ff3033d705c88bbcf0ea060568fdc20ca37",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293476,
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
      "evaluated_at": 1760293476
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
  "sig": "5a9152a6b1341b08808fa39778703d6084aba4582a6e9f024b597bba4caaa0b6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274446776
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 219, 'threshold': 50, 'total_amount': 68685846, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 218, 'first_seen': 1760285765, 'matching_hash': '03cceccb7405bcab'}}}