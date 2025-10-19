```json
{
  "id": "664cde62d45a1b9d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293455,
  "host_pid": "9e6742732c60:1",
  "hash": "fe24ee5be3a9f4414577e90d10861d85515dc2ff850b7bea53914fb7635c8680",
  "cid": "QmV1fe24ee5be3a9f4414577e90d10861d85515dc2ff",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293455,
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
      "evaluated_at": 1760293455
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
  "sig": "57334ed5f57ce17141c516bd6f0ab11a2d0a5b477ff5ef5564bee547f4769798"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038087823
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 219, 'threshold': 50, 'total_amount': 92073951, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 218, 'first_seen': 1760285763, 'matching_hash': '9ca4fa9f5ff6e727'}}}