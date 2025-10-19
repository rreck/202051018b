```json
{
  "id": "36d3fd245461aa57",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287812,
  "host_pid": "9e6742732c60:1",
  "hash": "c1e38034242f8d92fba0faf3901a2dd8b7e2867d30f5e1a5e32efaf3b1974a6f",
  "cid": "QmV1c1e38034242f8d92fba0faf3901a2dd8b7e2867d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287812,
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
      "evaluated_at": 1760287812
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
  "sig": "9b66a56de3fd6cb054699c6c239cb30604a26009c0018781ebda4832324d57dd"
}
```

Fraud detected: duplicate_transaction (score: 90)
Transaction: 063100271976362
Details: {'velocity': {'fraud_detected': True, 'risk_score': 96, 'details': {'transaction_count': 73, 'threshold': 50, 'total_amount': 29487036, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 72, 'first_seen': 1760285764, 'matching_hash': 'fe2a7bcd9137a402'}}}}}}