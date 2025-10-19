```json
{
  "id": "b23724e3fe7443bf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294843,
  "host_pid": "9e6742732c60:1",
  "hash": "553d7c5ec42b196ec8f9f2be48795214a67f98afcfd98d7f132084ef0243f0b0",
  "cid": "QmV1553d7c5ec42b196ec8f9f2be48795214a67f98af",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294843,
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
      "evaluated_at": 1760294843
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
  "sig": "2590ac3cdc4051bc18474196bd6ed559c4abfc49c34e52f67e89f830a85355cf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247533282
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 36749510, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285765, 'matching_hash': '15ae64209d1fefcb'}}}