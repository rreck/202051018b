```json
{
  "id": "c9b67f2766eedc70",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286363,
  "host_pid": "9e6742732c60:1",
  "hash": "e0e573e23821ac2e1fcf18ce348752b40bc49ef77e2125744b36283831e2f30c",
  "cid": "QmV1e0e573e23821ac2e1fcf18ce348752b40bc49ef7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286363,
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
      "evaluated_at": 1760286363
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
  "sig": "96d25b603b02cb3af185c200cb93baec9561f98c46198e5c432473087dd7f00b"
}
```

Fraud detected: invalid_routing (score: 90)
Transaction: 060557484693193
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 22, 'first_seen': 1760285763, 'matching_hash': 'db8aeeee2135ece1'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '060557489', 'validation_error': 'Invalid routing number checksum'}}}