```json
{
  "id": "65ae5a680ab7ac74",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287218,
  "host_pid": "9e6742732c60:1",
  "hash": "9c325b2581e9b208b99f2a91883492fe566585c8e740cbfd8e64b272eaeda441",
  "cid": "QmV19c325b2581e9b208b99f2a91883492fe566585c8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287218,
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
      "evaluated_at": 1760287218
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
  "sig": "4b37dc8dc8f4ee74e3ac80fb8878bedad7e7ab0801badbb58c8a26053e6fe6f9"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 044000032369849
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 52, 'threshold': 50, 'total_amount': 21708752, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 51, 'first_seen': 1760285764, 'matching_hash': '11b86d7f8733bf3d'}}}