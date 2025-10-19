```json
{
  "id": "cb8449c5be5859b0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294841,
  "host_pid": "9e6742732c60:1",
  "hash": "009c74b42a6be0e2bd829b550025509ec45a0ce8b51b3ec142da48a4dc1c4906",
  "cid": "QmV1009c74b42a6be0e2bd829b550025509ec45a0ce8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294841,
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
      "evaluated_at": 1760294841
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
  "sig": "df44589613d847f4b42a7d29ab726b6b5ec62fbae6bbd11deaaecc7912a1a5ac"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 763245925890246
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 111250825, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285764, 'matching_hash': '634500dd7ac761f0'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '763245921', 'validation_error': 'Invalid routing number checksum'}}}