```json
{
  "id": "111e934ff90c6bd4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286061,
  "host_pid": "9e6742732c60:1",
  "hash": "a8d7a9c3c32fef477950b0e82c5003afe3158fe987cc1ce787901ce1d88990a2",
  "cid": "QmV1a8d7a9c3c32fef477950b0e82c5003afe3158fe9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286061,
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
      "evaluated_at": 1760286061
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
  "sig": "ffc400eaf6230f60933add7dd19ed42813979535b2616ff2221a7d599e77ab5f"
}
```

Fraud detected: invalid_routing (score: 90)
Transaction: 728187407566692
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 12, 'first_seen': 1760285764, 'matching_hash': '1da2d57caa7d5158'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '728187403', 'validation_error': 'Invalid routing number checksum'}}}