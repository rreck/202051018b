```json
{
  "id": "399a097f36c1f84c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286935,
  "host_pid": "9e6742732c60:1",
  "hash": "994eff173ca469216520ae8110cfa3932b6cfb43648de7abf84c79ff5baf3951",
  "cid": "QmV1994eff173ca469216520ae8110cfa3932b6cfb43",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286935,
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
      "evaluated_at": 1760286935
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
  "sig": "bc9190ee3f892230f7fce0334e5e3e69c126b4cc5f4bb2d696bea7aa874685c8"
}
```

Fraud detected: invalid_routing (score: 90)
Transaction: 011137004104696
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 41, 'first_seen': 1760285765, 'matching_hash': 'b4a76c6b789f42f2'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '011137004', 'validation_error': 'Invalid routing number checksum'}}}