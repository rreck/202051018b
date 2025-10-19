```json
{
  "id": "b15ae46b90523b9a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289931,
  "host_pid": "9e6742732c60:1",
  "hash": "688db2dca4e330d6911d22d0abb896afbf0ea3116f498d10d5325ad2722013ed",
  "cid": "QmV1688db2dca4e330d6911d22d0abb896afbf0ea311",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289931,
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
      "evaluated_at": 1760289931
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
  "sig": "7a3dcce65487afcf94c6f0a1a8ea8d77bdb17d36921e9e0eba0c28af9421821d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592795708
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 137, 'threshold': 50, 'total_amount': 62972187, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 136, 'first_seen': 1760285763, 'matching_hash': '6f9672c314113419'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}