```json
{
  "id": "794270325071a399",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293025,
  "host_pid": "9e6742732c60:1",
  "hash": "81f01f71af3af146cc4247f15662f8ec1f91e9d3e0ad8a8cde02bfa9f72bcacb",
  "cid": "QmV181f01f71af3af146cc4247f15662f8ec1f91e9d3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293025,
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
      "evaluated_at": 1760293025
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
  "sig": "09b62415c9b183df8a40b10c129c99111e6a91c78c2aa5254e8e408dbc61b1b6"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 020899457068496
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 210, 'threshold': 50, 'total_amount': 82826730, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 209, 'first_seen': 1760285764, 'matching_hash': '41b228ccdaf61559'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '020899456', 'validation_error': 'Invalid routing number checksum'}}}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}