```json
{
  "id": "b629b561ee1e247e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293066,
  "host_pid": "9e6742732c60:1",
  "hash": "fd80b92b553f5b0c6bed73fff19a86dbfb58cc8980b5910af0ec8895e1b9e61c",
  "cid": "QmV1fd80b92b553f5b0c6bed73fff19a86dbfb58cc89",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293066,
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
      "evaluated_at": 1760293066
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
  "sig": "783ed9fd137f2f4e59d842662c7e1a967b71b9339808e2b1756b4e9f35e20a9f"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 568426902254568
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 211, 'threshold': 50, 'total_amount': 81431652, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 210, 'first_seen': 1760285763, 'matching_hash': '885fc97ad7583ad3'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '568426909', 'validation_error': 'Invalid routing number checksum'}}}