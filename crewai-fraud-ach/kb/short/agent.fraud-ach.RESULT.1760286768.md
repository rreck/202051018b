```json
{
  "id": "cf7ec25eaf4766a1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286768,
  "host_pid": "9e6742732c60:1",
  "hash": "cb00e1e4c1b4f285cd0bc58603ce44a9630f66e0fe6cd7f605a6e3e1bd781c78",
  "cid": "QmV1cb00e1e4c1b4f285cd0bc58603ce44a9630f66e0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286768,
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
      "evaluated_at": 1760286768
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "d8279826df2a43ac706164587ef36f6a997eb6b96876a45c5ea563d9aab909f9"
}
```

Fraud detected: invalid_routing (score: 90)
Transaction: 357223800655087
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 35, 'first_seen': 1760285765, 'matching_hash': '6810f1ba8ee75217'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '357223803', 'validation_error': 'Invalid routing number checksum'}}}