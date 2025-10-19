```json
{
  "id": "c7384ec35b92a777",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289637,
  "host_pid": "9e6742732c60:1",
  "hash": "f4a7c7b7ba2d9503e5e7825b618a1313bd40cb124a8469d4d952384a6a25ea28",
  "cid": "QmV1f4a7c7b7ba2d9503e5e7825b618a1313bd40cb12",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289637,
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
      "evaluated_at": 1760289637
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
  "sig": "325a17e75cc58b67d72970f39db2a00f7de2864719f8da7e01aafb1cbcc0f0e8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591752071
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 129, 'threshold': 50, 'total_amount': 14119308, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 128, 'first_seen': 1760285763, 'matching_hash': 'afb8628b94bcbefe'}}}