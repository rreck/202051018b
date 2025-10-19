```json
{
  "id": "47b853052ffe784a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289356,
  "host_pid": "9e6742732c60:1",
  "hash": "ed4cd69a66a6edbdb382ac33131af45b86174f0371ecf2dcb96dba5089f4adeb",
  "cid": "QmV1ed4cd69a66a6edbdb382ac33131af45b86174f03",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289356,
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
      "evaluated_at": 1760289356
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
  "sig": "0a5f55e2bd60b3952b9bfe2a262ee03817afffb8c8b36740b9dd8f56663cdbe4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000020127754
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 121, 'threshold': 50, 'total_amount': 22762762, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 120, 'first_seen': 1760285763, 'matching_hash': '0e6816faa7d68d85'}}}