```json
{
  "id": "cd194e4672a80a48",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292885,
  "host_pid": "9e6742732c60:1",
  "hash": "6c4fc4355fd35021a42735dd171f7bc3ad1dd9aeee077aec1e7c31ad82a097c3",
  "cid": "QmV16c4fc4355fd35021a42735dd171f7bc3ad1dd9ae",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292885,
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
      "evaluated_at": 1760292885
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
  "sig": "3029fb1115a994423bbb550b9946f6a8c7b4e006e66032b948d520ddcea7da1c"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 098545588857560
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 207, 'threshold': 50, 'total_amount': 28077273, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 206, 'first_seen': 1760285764, 'matching_hash': '7b745f55cd5357b8'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '098545585', 'validation_error': 'Invalid routing number checksum'}}}