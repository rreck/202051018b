```json
{
  "id": "29d6bb7fd864b4a7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285775,
  "host_pid": "9e6742732c60:1",
  "hash": "8acc8be7038fe41677c46a23da5e9fcb72f2584fd29898a6bc8d664aa0820213",
  "cid": "QmV18acc8be7038fe41677c46a23da5e9fcb72f2584f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285775,
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
      "evaluated_at": 1760285775
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
  "sig": "8a1739eaf1640b1763fe1cedd90cbc324ca82e093e36a73ec22b3571c4ad0207"
}
```

Fraud detected: invalid_routing (score: 90)
Transaction: 929669860929959
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 1, 'first_seen': 1760285763, 'matching_hash': 'bbfcfb9a6aef8521'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '929669867', 'validation_error': 'Invalid routing number checksum'}}}