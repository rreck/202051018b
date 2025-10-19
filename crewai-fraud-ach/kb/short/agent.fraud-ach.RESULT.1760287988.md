```json
{
  "id": "8c973d5944e891ed",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287988,
  "host_pid": "9e6742732c60:1",
  "hash": "c95f68e02d74d3bde739689c416e1205ed19f7d138fc9777f1970c7ec2d80808",
  "cid": "QmV1c95f68e02d74d3bde739689c416e1205ed19f7d1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287988,
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
      "evaluated_at": 1760287988
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
  "sig": "33c0840386d6d48dcc4a6fcda45f2fe45895b43160d802249fc1e7f0bbe32fba"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 182683956982385
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 79, 'threshold': 50, 'total_amount': 11822113, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 78, 'first_seen': 1760285764, 'matching_hash': '0eeac2a2909779e4'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '182683957', 'validation_error': 'Invalid routing number checksum'}}}