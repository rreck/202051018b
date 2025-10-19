```json
{
  "id": "29a97225c8ee08ab",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292845,
  "host_pid": "9e6742732c60:1",
  "hash": "c57bacdd9829c85f60dd6580597005916da82d6aedb78bdcc7d3c8f239772446",
  "cid": "QmV1c57bacdd9829c85f60dd6580597005916da82d6a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292845,
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
      "evaluated_at": 1760292845
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
  "sig": "3b2d79b22c7ae791cf68e8285d2bf0fce1822e9b7bb0efcf0f3b5c78a6a7847a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599696280
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 282, 'threshold': 50, 'total_amount': 67162530, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 281, 'first_seen': 1760284979, 'matching_hash': '32fd26aee1bbbffc'}}}