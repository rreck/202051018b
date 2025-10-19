```json
{
  "id": "d9aaa9506f732870",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289639,
  "host_pid": "9e6742732c60:1",
  "hash": "33235d12b95609db84ade8482d4ca12773b58cc252d8719d95a5a4103b6ed36c",
  "cid": "QmV133235d12b95609db84ade8482d4ca12773b58cc2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289639,
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
      "evaluated_at": 1760289639
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
  "sig": "30daa5469f986edff0a0a69cb31c30dab361f78b0f85ef1d638dc6841d1c413e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596228885
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 129, 'threshold': 50, 'total_amount': 56997489, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 128, 'first_seen': 1760285763, 'matching_hash': '9b2dabf2ca05df4f'}}}