```json
{
  "id": "6496910e6eb2707d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286369,
  "host_pid": "9e6742732c60:1",
  "hash": "55ee00ba85fbc26490ac73fe36b02f8ad487115a3b820aea256959cf93d7ed0b",
  "cid": "QmV155ee00ba85fbc26490ac73fe36b02f8ad487115a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286369,
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
      "evaluated_at": 1760286369
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
  "sig": "6c3588aa9f750ee47bc5bd8412f48b161e80c6d9e2006f904cd900fdb348e9ae"
}
```

Fraud detected: invalid_routing (score: 90)
Transaction: 612898027160979
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 22, 'first_seen': 1760285763, 'matching_hash': '1a410ec770966ef8'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '612898023', 'validation_error': 'Invalid routing number checksum'}}}sh': '445784114b53d57b'}}}