```json
{
  "id": "ed77e8913dda91a8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286695,
  "host_pid": "9e6742732c60:1",
  "hash": "eb1cf2d71b07d3d3a1a5e8c6975ab76a2be0651da8a4808a6c09dcfbd0f9d5d3",
  "cid": "QmV1eb1cf2d71b07d3d3a1a5e8c6975ab76a2be0651d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286695,
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
      "evaluated_at": 1760286695
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
  "sig": "d4aedafb9e70314ae1f1eaa5044844e6bfa806d63640fdd66b7f255a673b47e0"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 498752223480159
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 13388962, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 33, 'first_seen': 1760285763, 'matching_hash': '492624c5b9a9c8c0'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '498752220', 'validation_error': 'Invalid routing number checksum'}}}