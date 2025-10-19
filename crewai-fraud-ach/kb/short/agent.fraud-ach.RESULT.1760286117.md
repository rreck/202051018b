```json
{
  "id": "5640b6eeb50e7b7f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286117,
  "host_pid": "9e6742732c60:1",
  "hash": "289bb1d4771fa7f215626738a8d21bf5f7c438c2eab9317d61dc6e394d055b24",
  "cid": "QmV1289bb1d4771fa7f215626738a8d21bf5f7c438c2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286117,
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
      "evaluated_at": 1760286117
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "0722f21d74c05ce0b7e399f0c83e85919115c0bb5c575e70883d86db46778104"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000029518652
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 14, 'first_seen': 1760285763, 'matching_hash': 'e772ab4f6c2a0903'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '408733730', 'validation_error': 'Invalid routing number checksum'}}}