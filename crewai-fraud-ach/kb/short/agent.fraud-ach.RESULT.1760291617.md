```json
{
  "id": "31b03f882ef0601c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291617,
  "host_pid": "9e6742732c60:1",
  "hash": "b13891120e310825fa2bf0e3f8f0fe40e9fd73b6263e1644082a5c0535eddb62",
  "cid": "QmV1b13891120e310825fa2bf0e3f8f0fe40e9fd73b6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291617,
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
      "evaluated_at": 1760291617
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
  "sig": "cb471f59d6b012d550c8c84609a4348cb45fec4d6162ed563b81cf5276565e99"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 291093508895399
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 179, 'threshold': 50, 'total_amount': 85008532, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 178, 'first_seen': 1760285763, 'matching_hash': 'b750a26a60b25ace'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '291093507', 'validation_error': 'Invalid routing number checksum'}}}