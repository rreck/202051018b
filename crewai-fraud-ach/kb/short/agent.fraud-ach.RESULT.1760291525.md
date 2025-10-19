```json
{
  "id": "1177f3565f3ed172",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291525,
  "host_pid": "9e6742732c60:1",
  "hash": "e3622d9e10f82a11383545356772f9dfbe23b0405b9cfb19821ddf99e7043773",
  "cid": "QmV1e3622d9e10f82a11383545356772f9dfbe23b040",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291525,
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
      "evaluated_at": 1760291525
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
  "sig": "3729259e2ec4282bc25db02312af035ae27de411281e1c6a5a67bfd1090e9668"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 614505621863127
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 177, 'threshold': 50, 'total_amount': 49135554, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 176, 'first_seen': 1760285764, 'matching_hash': '8748c624c8dfcb5e'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '614505622', 'validation_error': 'Invalid routing number checksum'}}}