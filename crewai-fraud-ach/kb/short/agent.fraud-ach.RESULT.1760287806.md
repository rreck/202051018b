```json
{
  "id": "d92a2fd66fccac8d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287806,
  "host_pid": "9e6742732c60:1",
  "hash": "d0f7d34ec1a0b99f2a9d9299aed4f41ab508d401c98ebb76edb5ca3cf9786753",
  "cid": "QmV1d0f7d34ec1a0b99f2a9d9299aed4f41ab508d401",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287806,
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
      "evaluated_at": 1760287806
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
  "sig": "f65fbad4f34c33972fefe833c0e1d089b0d2098b022c2ea14564f5bc941764a8"
}
```

Fraud detected: duplicate_transaction (score: 90)
Transaction: 063100271177223
Details: {'velocity': {'fraud_detected': True, 'risk_score': 96, 'details': {'transaction_count': 73, 'threshold': 50, 'total_amount': 35307034, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 72, 'first_seen': 1760285763, 'matching_hash': 'bfc9cdfd9eceb164'}}}