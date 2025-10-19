```json
{
  "id": "d50fc652d2699c2e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290558,
  "host_pid": "9e6742732c60:1",
  "hash": "1a35a478c0cc2b162bed544b056addb5088333f3cd99b50a46c13cf8896ae729",
  "cid": "QmV11a35a478c0cc2b162bed544b056addb5088333f3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290558,
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
      "evaluated_at": 1760290558
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
  "sig": "c322688a2ab4c172c3b00dd05a8fd4d0afea97f184da44fa63508c1df04142fc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029278927
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 153, 'threshold': 50, 'total_amount': 44213022, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 152, 'first_seen': 1760285765, 'matching_hash': '45338af8ff50831c'}}}