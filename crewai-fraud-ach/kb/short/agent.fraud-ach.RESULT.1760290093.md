```json
{
  "id": "8587942b2cc2ae65",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290093,
  "host_pid": "9e6742732c60:1",
  "hash": "089b0c7e4697d6ba6805170a2ded288298a2b5c1dc6932b54887bc56da491e1d",
  "cid": "QmV1089b0c7e4697d6ba6805170a2ded288298a2b5c1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290093,
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
      "evaluated_at": 1760290093
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
  "sig": "28511ed4a8fc2bfd9fd1bfaff02ce4e85a129ba660cdeb904e61014bbad7f38c"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 818590551241151
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 141, 'threshold': 50, 'total_amount': 35965293, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 140, 'first_seen': 1760285763, 'matching_hash': '902b02e4e6ce46b6'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '818590557', 'validation_error': 'Invalid routing number checksum'}}}