```json
{
  "id": "38aad9ddc7ebeea4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294761,
  "host_pid": "9e6742732c60:1",
  "hash": "e2b4ca43525c5b5e8fadeed77487db772236531600df29ecec95e15af16e390c",
  "cid": "QmV1e2b4ca43525c5b5e8fadeed77487db7722365316",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294761,
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
      "evaluated_at": 1760294761
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
  "sig": "f8bbe69414365fd290acb9ecec674734ce8702e597872961f95e1b464fddec45"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247026993
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 107416852, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285764, 'matching_hash': '7c7d13001f766fd7'}}}