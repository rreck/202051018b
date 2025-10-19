```json
{
  "id": "ab7d1f2461e27794",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293829,
  "host_pid": "9e6742732c60:1",
  "hash": "e8bbfc9150e8931ab107505bf8e252378890c740db0818aa810900027703eccd",
  "cid": "QmV1e8bbfc9150e8931ab107505bf8e252378890c740",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293829,
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
      "evaluated_at": 1760293829
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
  "sig": "7fa0742a41138ab41c1fdb23f6eb54a7bfc6bb9fd31a89f79c2fc5599920f5c8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598290210
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 14479142, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285765, 'matching_hash': '255d3759171e1aec'}}}