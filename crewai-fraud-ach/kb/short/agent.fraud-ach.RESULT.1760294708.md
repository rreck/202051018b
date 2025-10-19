```json
{
  "id": "92c6a62546c0034b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294708,
  "host_pid": "9e6742732c60:1",
  "hash": "f056c7d44ec490af9445fa9db97dc919eb970f13efc71a58d3a670d9f07f7f70",
  "cid": "QmV1f056c7d44ec490af9445fa9db97dc919eb970f13",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294708,
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
      "evaluated_at": 1760294708
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
  "sig": "758bbe62cefd62dfcc7d05ad4b7d14c56cdab402d7efcb9a1523c3948bd522d5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000021715081
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 55531818, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285764, 'matching_hash': '0ea9b1b5c7891ffe'}}}