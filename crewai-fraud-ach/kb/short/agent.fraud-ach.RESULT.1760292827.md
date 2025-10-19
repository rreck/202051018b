```json
{
  "id": "286223451d6a9f2f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292827,
  "host_pid": "9e6742732c60:1",
  "hash": "ea474cb7e7d09e94fe0822b127c3076786ccb83925cd958a4b8cf34447c45f9b",
  "cid": "QmV1ea474cb7e7d09e94fe0822b127c3076786ccb839",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292827,
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
      "evaluated_at": 1760292827
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
  "sig": "ee0f279075055e7e7382c173e57850b1338d17de1cbf47503ae361ca819d4c39"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 361190719534797
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 206, 'threshold': 50, 'total_amount': 72008536, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 205, 'first_seen': 1760285763, 'matching_hash': '0d1ced523145a886'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '361190711', 'validation_error': 'Invalid routing number checksum'}}}