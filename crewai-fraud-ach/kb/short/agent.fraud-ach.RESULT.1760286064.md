```json
{
  "id": "ce73b56ea83afd5c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286064,
  "host_pid": "9e6742732c60:1",
  "hash": "d9ccadf423e4f7a91707f6762931ed1d15fc0df07f09f7e74331b6194e63858c",
  "cid": "QmV1d9ccadf423e4f7a91707f6762931ed1d15fc0df0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286064,
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
      "evaluated_at": 1760286064
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
  "sig": "e429c1245c9aa748ca75681dccd49613db8578e87d06f337105ede9c782ef288"
}
```

Fraud detected: invalid_routing (score: 90)
Transaction: 612898027160979
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 12, 'first_seen': 1760285763, 'matching_hash': '1a410ec770966ef8'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '612898023', 'validation_error': 'Invalid routing number checksum'}}}sh': 'c71937e0bf846771'}}}