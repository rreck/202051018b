```json
{
  "id": "d22c66a5d05e953e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294889,
  "host_pid": "9e6742732c60:1",
  "hash": "170593178d2e29f6f9ae88bef491f16db39d46fd9cfc4ad6cfad6862a4e1f657",
  "cid": "QmV1170593178d2e29f6f9ae88bef491f16db39d46fd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294889,
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
      "evaluated_at": 1760294889
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
  "sig": "660e4fdd4ba2fea905ddd9c708882dd6d2c39ae6093fa0374849e121cbd78202"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029163318
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 75880422, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285765, 'matching_hash': 'b5567c8565e47211'}}}