```json
{
  "id": "d79ef864fb2a25b3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287924,
  "host_pid": "9e6742732c60:1",
  "hash": "e8c503c6d61d2d535a109b992b504ce9e8f77dd30e7f5792b1a92e03f952b3d0",
  "cid": "QmV1e8c503c6d61d2d535a109b992b504ce9e8f77dd3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287924,
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
      "evaluated_at": 1760287924
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
  "sig": "7c2d582e8c7a4e78735b04edc86973536761141a4629ee501e7e27f84de3d6d5"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 580123061332551
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 77, 'threshold': 50, 'total_amount': 16212735, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 76, 'first_seen': 1760285763, 'matching_hash': 'b65f94a39c8828ce'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '580123066', 'validation_error': 'Invalid routing number checksum'}}}