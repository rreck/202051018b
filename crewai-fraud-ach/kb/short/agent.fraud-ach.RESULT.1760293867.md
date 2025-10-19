```json
{
  "id": "a4938b07f8858ccb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293867,
  "host_pid": "9e6742732c60:1",
  "hash": "9af5b38efeeb5072a1f3956e292c711527f0aaa16b60ea4ba63a77138eba9c45",
  "cid": "QmV19af5b38efeeb5072a1f3956e292c711527f0aaa1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293867,
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
      "evaluated_at": 1760293867
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
  "sig": "03bc037c2b0f2407164d0c294483b2443ed7c75751eec705d3fca0ae7363fdcd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022243585
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 11717059, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285764, 'matching_hash': '763c66b493018133'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '691661790', 'validation_error': 'Invalid routing number checksum'}}}