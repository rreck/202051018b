```json
{
  "id": "222dc8f99aeea5b6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285144,
  "host_pid": "9e6742732c60:1",
  "hash": "ce2d1b3d3c42324c55ab3410ba81260d690a4981b5ce34a895d64426be28c2b5",
  "cid": "QmV1ce2d1b3d3c42324c55ab3410ba81260d690a4981",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285144,
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
      "evaluated_at": 1760285144
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
  "sig": "0b6c54f75cb6119b691371a43bf63b80cec7f3bcde0efb68a83d341a318ee593"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000026203898
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 16, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}