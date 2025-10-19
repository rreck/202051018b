```json
{
  "id": "7b6a9124478822ab",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287660,
  "host_pid": "9e6742732c60:1",
  "hash": "efdc683bae4632b8d84668665d12519f5ac27c519a3123f620436ed4041769b9",
  "cid": "QmV1efdc683bae4632b8d84668665d12519f5ac27c51",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287660,
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
      "evaluated_at": 1760287660
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
  "sig": "78f19e196171bd2b1d00a8e384d30d03d5c495cac70a7812a7178240bb557f39"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000028760265
Details: {'velocity': {'fraud_detected': True, 'risk_score': 86, 'details': {'transaction_count': 68, 'threshold': 50, 'total_amount': 18899240, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 67, 'first_seen': 1760285763, 'matching_hash': 'ff1172b8afcaa4bc'}}}