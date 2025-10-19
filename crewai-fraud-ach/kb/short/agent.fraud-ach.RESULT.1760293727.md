```json
{
  "id": "f067f48f9685b18a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293727,
  "host_pid": "9e6742732c60:1",
  "hash": "d08530fcb55cc27885088bd3f9f5f05493a7fbbfbd5cdb84c5ad8452787bb91a",
  "cid": "QmV1d08530fcb55cc27885088bd3f9f5f05493a7fbbf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293727,
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
      "evaluated_at": 1760293727
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
  "sig": "f79fa218ae570f1436f7f954230083ee2e96c190d80514be0c356ae60dbbd321"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022148998
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 224, 'threshold': 50, 'total_amount': 62273344, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 223, 'first_seen': 1760285765, 'matching_hash': 'cc8f74c02d21ef44'}}}