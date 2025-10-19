```json
{
  "id": "dab1800ef1a0ca8a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286824,
  "host_pid": "9e6742732c60:1",
  "hash": "41069fed97cd1ec9a4ef1d9df72e874d06f9dbab57d93370d4f10f023b4e80d0",
  "cid": "QmV141069fed97cd1ec9a4ef1d9df72e874d06f9dbab",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286824,
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
      "evaluated_at": 1760286824
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "c7a586edc242b5822442842ce14d9d1ca3b20ab7ed1f42647bd7921fa80e37d0"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201465822757
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 17202562, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 37, 'first_seen': 1760285765, 'matching_hash': '1a67314a077331d2'}}}