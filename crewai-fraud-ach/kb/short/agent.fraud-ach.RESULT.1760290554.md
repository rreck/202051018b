```json
{
  "id": "a25249db38e7d15b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290554,
  "host_pid": "9e6742732c60:1",
  "hash": "d96f4819f5c0cd022e2b49d2e55426d8a3cca7c16ceb96bc68c7ad06858cd7a8",
  "cid": "QmV1d96f4819f5c0cd022e2b49d2e55426d8a3cca7c1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290554,
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
      "evaluated_at": 1760290554
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
  "sig": "bef726915cbce93efd80c2e9a7aba3fab9e237c9589d052b10de58afa1a938de"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153312612
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 153, 'threshold': 50, 'total_amount': 15300000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 152, 'first_seen': 1760285763, 'matching_hash': 'b6b1aeb6185e45bf'}}}