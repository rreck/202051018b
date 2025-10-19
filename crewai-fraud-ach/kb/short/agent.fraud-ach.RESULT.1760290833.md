```json
{
  "id": "7572f63200ca906d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290833,
  "host_pid": "9e6742732c60:1",
  "hash": "c1962a84cb9ea33d4cd9c0c9956fda49602595ec0a9485596e48a01065943c2c",
  "cid": "QmV1c1962a84cb9ea33d4cd9c0c9956fda49602595ec",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290833,
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
      "evaluated_at": 1760290833
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
  "sig": "fb09eb0e1a67ca241d43a0ed4988e1373d3cf9ed605ff6dc04275988948187e0"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 009592678117470
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 160, 'threshold': 50, 'total_amount': 19378240, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 159, 'first_seen': 1760285764, 'matching_hash': 'f5249213623024b2'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '009592679', 'validation_error': 'Invalid routing number checksum'}}}