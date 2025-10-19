```json
{
  "id": "de244025c8b9032d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287518,
  "host_pid": "9e6742732c60:1",
  "hash": "c8c0356c279f80d238566d1ce194eeec4d2646cacae0cfa85a61bbd45b08ab16",
  "cid": "QmV1c8c0356c279f80d238566d1ce194eeec4d2646ca",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287518,
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
      "evaluated_at": 1760287518
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
  "sig": "b66475dcf4cc847e9240ba73abfa9f07428d1486b4da76882630a11b3f1b2e1b"
}
```

Fraud detected: invalid_routing (score: 85)
Transaction: 098545588857560
Details: {'velocity': {'fraud_detected': True, 'risk_score': 76, 'details': {'transaction_count': 63, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 62, 'first_seen': 1760285764, 'matching_hash': '7b745f55cd5357b8'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '098545585', 'validation_error': 'Invalid routing number checksum'}}}