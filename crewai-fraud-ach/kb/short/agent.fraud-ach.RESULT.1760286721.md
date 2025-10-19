```json
{
  "id": "b1b401f03c8ab499",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286721,
  "host_pid": "9e6742732c60:1",
  "hash": "1aa5ba8d37c09de0c0aeede1d9ec2645fde95267702037ba7ef25ed197c3cecd",
  "cid": "QmV11aa5ba8d37c09de0c0aeede1d9ec2645fde95267",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286721,
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
      "evaluated_at": 1760286721
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
  "sig": "ddbfa175cd15b0f6a67cc1728d31984e5dfc8ecd516c9257ee4ac97c3ff0653f"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 568426902254568
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 13507620, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 34, 'first_seen': 1760285763, 'matching_hash': '885fc97ad7583ad3'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '568426909', 'validation_error': 'Invalid routing number checksum'}}}